# Leonida Companion

Mappa companion personale e non ufficiale per GTA 6 (PS5): negozi e servizi, auto rare e nascoste, cose da non perdere per ogni capitolo (punti di non ritorno), Easter egg e i tuoi pin. Ogni voce ha i link alle guide. Le spunte restano salvate nel browser; dal pannello «Mappa» puoi copiare un backup.

Funziona come sito statico: apri `index.html` da GitHub Pages (Settings → Pages → Deploy from a branch → `main` / root).

## Contenuto

- `index.html` – l'app (Leaflet, nessun server)
- `data.json` – negozi, auto, capitoli, Easter egg, indice di ricerca
- `tiles/` (livelli 0–3, blocchi 1024 px) e `big/` (livelli 4–5, blocchi 2048 px) – la mappa
- `tools/` – script per rigenerare tile e dati dal repository di GTADB

## Crediti e licenze

- Mappa e luoghi: **GTA VI Map Tiles (CC BY 4.0) — https://map.gtadb.org** e **GTA VI Landmarks Data (CC BY 4.0) — https://map.gtadb.org**, © GTADB.ORG e contributori ([repository](https://github.com/rolux/gtadb.org)). Le tile sono state ricomposte in blocchi più grandi e i luoghi filtrati e tradotti. Licenza: https://creativecommons.org/licenses/by/4.0/
- Grafica della mappa di gioco: Rockstar Games.
- Leaflet 1.9.4 (BSD-2-Clause).
- Auto, missabili ed Easter egg sono riassunti dalle guide citate dentro l'app, ciascuna con il suo link.

Progetto non ufficiale, senza legami con Rockstar Games o Take-Two.
