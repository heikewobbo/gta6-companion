# Leonida Companion

Mappa companion personale e non ufficiale per GTA 6 (PS5): negozi e servizi, auto rare e nascoste, tutte le missioni (storia, facoltative, Strangers & Freaks) con pin dove si conosce la partenza, cose da non perdere per ogni capitolo (punti di non ritorno), Easter egg e i tuoi pin. Scegli in alto il capitolo a cui sei: mappa e liste mostrano solo quello che è già sbloccato (rifugi, ricettatori, auto che richiedono strumenti dei capitoli successivi) e un riquadro elenca le novità di ogni capitolo. Ogni voce ha i link alle guide. Le spunte restano salvate nel browser; dal pannello «Mappa» salvi e ricarichi un file di backup (.json). Su iPhone: Safari → Condividi → «Aggiungi alla schermata Home» per averla come app con la sua icona.

Funziona come sito statico: apri `index.html` da GitHub Pages (Settings → Pages → Deploy from a branch → `main` / root).

## Trofei automatici (PlayStation e Xbox)

Ognuno scrive nell'app (scheda Trofei) il proprio ID PSN o gamertag Xbox e i trofei si spuntano da soli. A leggerli è un piccolo Cloudflare Worker gratuito (`worker/trofei-worker.js`) che tiene al sicuro i segreti e chiede i dati a Sony e, per Xbox, a OpenXBL. Le risposte restano in memoria 10 minuti.

1. Crea un account gratuito su https://dash.cloudflare.com.
2. Workers & Pages → Create application → GitHub (autorizza l'accesso) → scegli `gta6-companion`.
3. Configurazione: nome del progetto `leonida-trofei` (deve essere uguale a `name` in `wrangler.jsonc`), Build command vuoto, Deploy command `npx wrangler deploy`. Poi Deploy. Da ora ogni modifica sul repo ripubblica il Worker da sola.
4. Nel Worker: Settings → Variables and Secrets → Add, tipo **Secret**:
   - `PSN_NPSSO`: il token npsso da https://ca.account.sony.com/api/v1/ssocookie (dopo l'accesso su playstation.com, nello stesso browser);
   - `XBL_KEY` (solo per Xbox): la chiave API di https://xbl.io (accesso con un account Microsoft, piano gratuito).
   `ALLOWED_ORIGIN` è già in `wrangler.jsonc`.
5. Copia l'indirizzo del Worker (es. `https://leonida-trofei.NOME.workers.dev`) e scrivilo in `psn/config.json`: `{"api": "https://leonida-trofei.NOME.workers.dev/"}`.
6. Prova: apri `https://leonida-trofei.NOME.workers.dev/?id=TuoIDPSN` (o `?xbox=Gamertag`): deve rispondere con l'elenco dei trofei.

Ogni giocatore deve avere trofei/obiettivi visibili a tutti nelle impostazioni privacy. Il token PSN scade dopo circa due mesi: quando l'app segnala «token PSN non valido o scaduto», ripeti il punto 3 per `PSN_NPSSO`. Sony e OpenXBL sono interfacce non ufficiali, usate solo in lettura.

## Contenuto

- `index.html` – l'app (Leaflet, nessun server)
- `data.json` – negozi, auto, capitoli, Easter egg, indice di ricerca
- `tiles/` (livelli 0–3, blocchi 1024 px) e `big/` (livelli 4–5, blocchi 2048 px) – la mappa
- `sw.js`, `tiles.json` – funzionamento offline (mappa salvabile dal pannello Mappa)
- `worker/trofei-worker.js`, `psn/config.json` – trofei automatici da PSN e Xbox (Cloudflare Worker)
- `icons/`, `manifest.webmanifest` – icona e dati per l'installazione sulla schermata Home
- `tools/` – script per rigenerare tile e dati dal repository di GTADB, elenchi missioni, sorgente dell'icona

## Crediti e licenze

- Mappa e luoghi: **GTA VI Map Tiles (CC BY 4.0) — https://map.gtadb.org** e **GTA VI Landmarks Data (CC BY 4.0) — https://map.gtadb.org**, © GTADB.ORG e contributori ([repository](https://github.com/rolux/gtadb.org)). Le tile sono state ricomposte in blocchi più grandi e i luoghi filtrati e tradotti. Licenza: https://creativecommons.org/licenses/by/4.0/
- Grafica della mappa di gioco: Rockstar Games.
- Leaflet 1.9.4 (BSD-2-Clause).
- Elenco missioni e link ai walkthrough: PowerPyx. Auto, missabili ed Easter egg sono riassunti dalle guide citate dentro l'app, ciascuna con il suo link.

Progetto non ufficiale, senza legami con Rockstar Games o Take-Two.
