# Leonida Companion

Mappa companion personale e non ufficiale per GTA 6 (PS5): negozi e servizi, auto rare e nascoste, tutte le missioni (storia, facoltative, Strangers & Freaks) con pin dove si conosce la partenza, cose da non perdere per ogni capitolo (punti di non ritorno), Easter egg e i tuoi pin. Scegli in alto il capitolo a cui sei: mappa e liste mostrano solo quello che è già sbloccato (rifugi, ricettatori, auto che richiedono strumenti dei capitoli successivi) e un riquadro elenca le novità di ogni capitolo. Ogni voce ha i link alle guide. Le spunte restano salvate nel browser; dal pannello «Mappa» salvi e ricarichi un file di backup (.json). Su iPhone: Safari → Condividi → «Aggiungi alla schermata Home» per averla come app con la sua icona.

Funziona come sito statico: apri `index.html` da GitHub Pages (Settings → Pages → Deploy from a branch → `main` / root).

## Contenuto

- `index.html` – l'app (Leaflet, nessun server)
- `data.json` – negozi, auto, capitoli, Easter egg, indice di ricerca
- `tiles/` (livelli 0–3, blocchi 1024 px) e `big/` (livelli 4–5, blocchi 2048 px) – la mappa
- `icons/`, `manifest.webmanifest` – icona e dati per l'installazione sulla schermata Home
- `tools/` – script per rigenerare tile e dati dal repository di GTADB, elenchi missioni, sorgente dell'icona

## Crediti e licenze

- Mappa e luoghi: **GTA VI Map Tiles (CC BY 4.0) — https://map.gtadb.org** e **GTA VI Landmarks Data (CC BY 4.0) — https://map.gtadb.org**, © GTADB.ORG e contributori ([repository](https://github.com/rolux/gtadb.org)). Le tile sono state ricomposte in blocchi più grandi e i luoghi filtrati e tradotti. Licenza: https://creativecommons.org/licenses/by/4.0/
- Grafica della mappa di gioco: Rockstar Games.
- Leaflet 1.9.4 (BSD-2-Clause).
- Elenco missioni e link ai walkthrough: PowerPyx. Auto, missabili ed Easter egg sono riassunti dalle guide citate dentro l'app, ciascuna con il suo link.

Progetto non ufficiale, senza legami con Rockstar Games o Take-Two.
