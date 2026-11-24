// Leonida Companion: trofei/obiettivi di GTA VI da PSN e Xbox per qualsiasi giocatore.
// Cloudflare Worker. Variabili: PSN_NPSSO (segreto, token PSN dell'account che legge i trofei),
// XBL_KEY (segreto, chiave OpenXBL da xbl.io, solo per Xbox), ALLOWED_ORIGIN (es. https://heikewobbo.github.io).
// Uso: GET https://<worker>/?id=IDPSN   oppure   GET https://<worker>/?xbox=Gamertag
const AUTH = "https://ca.account.sony.com/api/authz/v3/oauth";
const BASIC = "Basic MDk1MTUxNTktNzIzNy00MzcwLTliNDAtMzgwNmU2N2MwODkxOnVjUGprYTV0bnRCMktxc1A=";
const REDIRECT = "com.scee.psxandroid.scecompcall://redirect";
const TROPHY = "https://m.np.playstation.com/api/trophy";
const PROFILE = "https://us-prof.np.community.playstation.net/userProfile/v1/users";
const CACHE_SECONDS = 600;

let tok = null, names = null;

async function accessToken(env) {
  if (tok && tok.exp > Date.now() + 60000) return tok.access;
  if (!env.PSN_NPSSO) throw new Error("manca il segreto PSN_NPSSO");
  const q = new URLSearchParams({ access_type: "offline", client_id: "09515159-7237-4370-9b40-3806e67c0891", redirect_uri: REDIRECT, response_type: "code", scope: "psn:mobile.v2.core psn:clientapp" });
  const r = await fetch(`${AUTH}/authorize?${q}`, { headers: { Cookie: `npsso=${env.PSN_NPSSO}` }, redirect: "manual" });
  const loc = r.headers.get("location") || "";
  if (!loc.includes("?code=")) throw new Error("token PSN non valido o scaduto: rinnova PSN_NPSSO");
  const code = new URLSearchParams(loc.split("redirect/")[1]).get("code");
  const t = await (await fetch(`${AUTH}/token`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded", Authorization: BASIC },
    body: new URLSearchParams({ code, redirect_uri: REDIRECT, grant_type: "authorization_code", token_format: "jwt" }).toString()
  })).json();
  if (!t.access_token) throw new Error("accesso al PSN non riuscito");
  tok = { access: t.access_token, exp: Date.now() + (t.expires_in || 3600) * 1000 };
  return tok.access;
}

async function psn(url, a) {
  const r = await fetch(url, { headers: { Authorization: `Bearer ${a}` } });
  const j = await r.json().catch(() => ({}));
  if (j.error) throw new Error(j.error.message || "errore del PSN");
  return j;
}

async function trophiesFor(id, env) {
  const a = await accessToken(env);
  let accountId;
  try { accountId = (await psn(`${PROFILE}/${encodeURIComponent(id)}/profile2?fields=accountId,onlineId`, a)).profile.accountId; }
  catch { throw new Error("ID PSN non trovato"); }
  const titles = await psn(`${TROPHY}/v1/users/${accountId}/trophyTitles?limit=800`, a);
  const title = (titles.trophyTitles || []).find(t => String(t.trophyTitleName).toLowerCase().replace(/[^a-z0-9 ]/g, "").trim().startsWith("grand theft auto vi"));
  if (!title) throw new Error("GTA VI non trovato: trofei privati o nessun trofeo ancora");
  const svc = `npServiceName=${title.npServiceName}`;
  if (!names) {
    const all = await psn(`${TROPHY}/v1/npCommunicationIds/${title.npCommunicationId}/trophyGroups/all/trophies?${svc}`, a);
    names = new Map(all.trophies.map(t => [t.trophyId, t.trophyName]));
  }
  const mine = await psn(`${TROPHY}/v1/users/${accountId}/npCommunicationIds/${title.npCommunicationId}/trophyGroups/all/trophies?${svc}`, a);
  const earned = mine.trophies.filter(t => t.earned).map(t => names.get(t.trophyId)).filter(Boolean).sort();
  return { player: id, title: title.trophyTitleName, progress: title.progress ?? null, earned, updated: new Date().toISOString() };
}

// --- Xbox (OpenXBL, non ufficiale) ---
const XBL = "https://api.xbl.io/api/v2";
async function xbl(path, env) {
  if (!env.XBL_KEY) throw new Error("Xbox non configurato: manca il segreto XBL_KEY");
  const r = await fetch(XBL + path, { headers: { "X-Authorization": env.XBL_KEY, Accept: "application/json", "Accept-Language": "en-US" } });
  if (r.status === 429) throw new Error("troppe richieste a OpenXBL, riprova tra poco");
  if (r.status === 404) throw new Error("Gamertag non trovato");
  if (!r.ok) throw new Error("OpenXBL ha risposto " + r.status);
  return r.json();
}
const pick = (...v) => v.find(x => x !== undefined && x !== null && x !== "");
async function xboxFor(tag, env) {
  const prof = await xbl(`/player/gamertag/${encodeURIComponent(tag)}`, env);
  const u = prof.profileUsers?.[0] || prof.people?.[0] || prof.content?.people?.[0] || prof;
  const xuid = pick(u.xuid, u.id, u.xuId);
  if (!xuid) throw new Error("Gamertag non trovato");
  const hist = await xbl(`/player/titleHistory/${xuid}`, env);
  const list = hist.titles || hist.content?.titles || [];
  const title = list.find(t => String(pick(t.name, t.titleName, "")).toLowerCase().replace(/[^a-z0-9 ]/g, "").trim().startsWith("grand theft auto vi"));
  if (!title) throw new Error("GTA VI non trovato tra i giochi di questo gamertag (profilo privato o nessun obiettivo ancora)");
  const ach = await xbl(`/achievements/player/${xuid}/title/${pick(title.titleId, title.id)}`, env);
  const items = ach.achievements || ach.content?.achievements || [];
  const earned = items.filter(a => a.progressState === "Achieved" || a.unlocked === true).map(a => a.name).filter(Boolean).sort();
  return { player: tag, platform: "xbox", title: pick(title.name, title.titleName), earned, updated: new Date().toISOString() };
}

export default {
  async fetch(request, env, ctx) {
    const cors = { "Access-Control-Allow-Origin": env.ALLOWED_ORIGIN || "*", "Access-Control-Allow-Methods": "GET", "Content-Type": "application/json; charset=utf-8" };
    if (request.method === "OPTIONS") return new Response(null, { headers: cors });
    const url = new URL(request.url), xbox = (url.searchParams.get("xbox") || "").trim(), id = xbox || (url.searchParams.get("id") || "").trim();
    if (xbox ? !/^[A-Za-z0-9 #]{1,20}$/.test(xbox) : !/^[A-Za-z][A-Za-z0-9_-]{2,15}$/.test(id)) return new Response(JSON.stringify({ error: xbox ? "Gamertag non valido" : "ID PSN non valido" }), { status: 400, headers: cors });
    const fresh = url.searchParams.has("fresh");
    const key = new Request(`${url.origin}/?${xbox ? "xbox" : "id"}=${encodeURIComponent(id.toLowerCase())}`);
    const cache = typeof caches !== "undefined" ? caches.default : null;
    if (cache && !fresh) { const hit = await cache.match(key); if (hit) return new Response(hit.body, { headers: cors }); }
    try {
      const body = JSON.stringify(xbox ? await xboxFor(xbox, env) : await trophiesFor(id, env));
      if (cache) ctx.waitUntil(cache.put(key, new Response(body, { headers: { "Cache-Control": `s-maxage=${CACHE_SECONDS}` } })));
      return new Response(body, { headers: cors });
    } catch (e) {
      return new Response(JSON.stringify({ player: id, earned: [], error: String(e.message || e) }), { status: 502, headers: cors });
    }
  }
};
