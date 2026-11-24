// Legge i trofei di GTA VI degli ID PSN in psn/players.json e scrive psn/<ID>.json.
// Gira su GitHub Actions con il segreto PSN_NPSSO (token dell'account di chi gestisce l'app).
import fs from "node:fs";
import {
  exchangeNpssoForAccessCode, exchangeAccessCodeForAuthTokens, getProfileFromUserName,
  makeUniversalSearch, getUserTitles, getTitleTrophies, getUserTrophiesEarnedForTitle
} from "psn-api";

const DIR = process.env.PSN_DIR || "psn";
const players = JSON.parse(fs.readFileSync(`${DIR}/players.json`, "utf8"));
const npsso = process.env.PSN_NPSSO;
if (!npsso) { console.error("Manca il segreto PSN_NPSSO"); process.exit(1); }
if (!players.length) { console.log("Nessun giocatore in psn/players.json"); process.exit(0); }

const auth = await exchangeAccessCodeForAuthTokens(await exchangeNpssoForAccessCode(npsso));
const isGta6 = t => String(t.trophyTitleName).toLowerCase().replace(/[^a-z0-9 ]/g, "").trim().startsWith("grand theft auto vi");

async function accountIdOf(name) {
  try { return (await getProfileFromUserName(auth, name)).profile.accountId; }
  catch {
    const r = await makeUniversalSearch(auth, name, "SocialAllAccounts");
    const hit = r.domainResponses?.[0]?.results?.find(x => x.socialMetadata?.onlineId?.toLowerCase() === name.toLowerCase());
    if (!hit) throw new Error("ID PSN non trovato");
    return hit.socialMetadata.accountId;
  }
}

let names = null;
for (const name of players) {
  const file = `${DIR}/${name}.json`;
  let out;
  try {
    const accountId = await accountIdOf(name);
    const titles = await getUserTitles(auth, accountId, { limit: 800 });
    const title = (titles.trophyTitles || []).find(isGta6);
    if (!title) throw new Error("GTA VI non trovato: trofei privati o nessun trofeo ancora");
    const opt = { npServiceName: title.npServiceName };
    if (!names) {
      const all = await getTitleTrophies(auth, title.npCommunicationId, "all", opt);
      names = new Map(all.trophies.map(t => [t.trophyId, t.trophyName]));
    }
    const mine = await getUserTrophiesEarnedForTitle(auth, accountId, title.npCommunicationId, "all", opt);
    const earned = mine.trophies.filter(t => t.earned).map(t => names.get(t.trophyId)).filter(Boolean).sort();
    out = { player: name, title: title.trophyTitleName, progress: title.progress ?? null, earned };
  } catch (e) {
    out = { player: name, earned: [], error: String(e.message || e) };
  }
  let old = null;
  try { old = JSON.parse(fs.readFileSync(file, "utf8")); } catch {}
  const same = old && JSON.stringify({ ...old, updated: 0 }) === JSON.stringify({ ...out, updated: 0 });
  if (!same) { fs.writeFileSync(file, JSON.stringify({ ...out, updated: new Date().toISOString() }, null, 1) + "\n"); console.log(`${name}: aggiornato (${out.earned.length} trofei${out.error ? ", " + out.error : ""})`); }
  else console.log(`${name}: nessun cambiamento`);
}
