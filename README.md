# Leonida Companion

Mappa companion personale e non ufficiale per GTA 6 (PS5): negozi e servizi, auto rare e nascoste, tutte le missioni (storia, facoltative, Strangers & Freaks) con pin dove si conosce la partenza, cose da non perdere per ogni capitolo (punti di non ritorno), Easter egg e i tuoi pin. Scegli in alto il capitolo a cui sei: mappa e liste mostrano solo quello che è già sbloccato (rifugi, ricettatori, auto che richiedono strumenti dei capitoli successivi) e un riquadro elenca le novità di ogni capitolo. Ogni voce ha i link alle guide. Le spunte restano salvate nel browser; dal pannello «Mappa» salvi e ricarichi un file di backup (.json). Su iPhone: Safari → Condividi → «Aggiungi alla schermata Home» per averla come app con la sua icona.

Funziona come sito statico: apri `index.html` da GitHub Pages (Settings → Pages → Deploy from a branch → `main` / root).

## Trofei automatici dal PSN (per più persone)

Uno script su GitHub Actions legge ogni ora i trofei di GTA VI degli ID PSN elencati e li salva in `psn/<ID>.json`. Nell'app, scheda Trofei, ognuno sceglie il proprio ID e i trofei si spuntano da soli. I trofei si leggono con l'account PSN di chi gestisce il repo, quindi serve un solo token.

1. **Token**: accedi a https://www.playstation.com dal browser, poi apri https://ca.account.sony.com/api/v1/ssocookie e copia il valore `npsso` (64 caratteri). Vale come una password: non metterlo mai nei file del repo.
2. **Segreto**: nel repo vai su Settings → Secrets and variables → Actions → New repository secret, nome `PSN_NPSSO`, valore il token.
3. **Giocatori**: modifica `psn/players.json` con gli ID PSN, per esempio `["MioID", "IDAmico"]`.
4. **Privacy**: ogni giocatore deve avere i trofei visibili (PS5 → Impostazioni → Utenti e account → Privacy → «Giochi | Trofei» su «Chiunque», oppure amico del tuo account).
5. **Prova**: Actions → Trofei PSN → Run workflow. Poi gira da solo ogni ora.

Il token scade dopo circa due mesi: quando nell'app compare un errore, ripeti i punti 1 e 2. Usa un'interfaccia non ufficiale di Sony (libreria psn-api), solo in lettura. I file in `psn/` sono pubblici come il resto del repo.

## Contenuto

- `index.html` – l'app (Leaflet, nessun server)
- `data.json` – negozi, auto, capitoli, Easter egg, indice di ricerca
- `tiles/` (livelli 0–3, blocchi 1024 px) e `big/` (livelli 4–5, blocchi 2048 px) – la mappa
- `sw.js`, `tiles.json` – funzionamento offline (mappa salvabile dal pannello Mappa)
- `psn/`, `tools/psn-sync.mjs`, `.github/workflows/trofei-psn.yml` – trofei automatici dal PSN
- `icons/`, `manifest.webmanifest` – icona e dati per l'installazione sulla schermata Home
- `tools/` – script per rigenerare tile e dati dal repository di GTADB, elenchi missioni, sorgente dell'icona

## Crediti e licenze

- Mappa e luoghi: **GTA VI Map Tiles (CC BY 4.0) — https://map.gtadb.org** e **GTA VI Landmarks Data (CC BY 4.0) — https://map.gtadb.org**, © GTADB.ORG e contributori ([repository](https://github.com/rolux/gtadb.org)). Le tile sono state ricomposte in blocchi più grandi e i luoghi filtrati e tradotti. Licenza: https://creativecommons.org/licenses/by/4.0/
- Grafica della mappa di gioco: Rockstar Games.
- Leaflet 1.9.4 (BSD-2-Clause).
- Elenco missioni e link ai walkthrough: PowerPyx. Auto, missabili ed Easter egg sono riassunti dalle guide citate dentro l'app, ciascuna con il suo link.

Progetto non ufficiale, senza legami con Rockstar Games o Take-Two.
