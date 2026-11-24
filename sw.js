// Leonida Companion: funziona anche offline. Le tile della mappa si salvano quando le vedi
// oppure tutte insieme dal pulsante «Salva la mappa per l'offline».
const CORE = "leonida-core-v1", TILES = "leonida-tiles-v1";
const CORE_FILES = ["./", "index.html", "data.json", "leaflet.js", "manifest.webmanifest", "icons/apple-touch-icon.png", "icons/icon-192.png", "icons/favicon-32.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CORE).then(c => c.addAll(CORE_FILES)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(k => Promise.all(k.filter(n => n !== CORE && n !== TILES).map(n => caches.delete(n)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  const req = e.request; if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin === location.origin && /\/(tiles|big)\//.test(url.pathname)) {
    e.respondWith(caches.open(TILES).then(async c => (await c.match(req)) || fetch(req).then(r => { if (r.ok) c.put(req, r.clone()); return r; })));
    return;
  }
  // tutto il resto: prima la rete (dati sempre aggiornati), se manca la connessione la copia salvata
  e.respondWith(fetch(req).then(r => { if (r.ok && (url.origin === location.origin || url.host.endsWith("gstatic.com") || url.host.endsWith("googleapis.com"))) { const cp = r.clone(); caches.open(CORE).then(c => c.put(req, cp)); } return r; })
    .catch(() => caches.match(req, {ignoreSearch: true}).then(r => r || (req.mode === "navigate" ? caches.match("index.html") : Response.error()))));
});
