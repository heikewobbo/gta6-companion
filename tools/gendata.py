import json, sys, statistics

lm = json.load(open(sys.argv[1]))
out = sys.argv[2]

def area(name):
    pts = [v[1] for v in lm.values() if v[1] and name.lower() in v[0].lower()]
    return [round(statistics.median(p[0] for p in pts)), round(statistics.median(p[1] for p in pts))]

def at(lid, dx=0, dy=0):
    x, y = lm[lid][1]
    return [round(x + dx), round(y + dy)]

CAT = {
    "#guns": ("armi", "Armi"), "#clothes": ("vestiti", "Vestiti"), "#shoes": ("vestiti", "Vestiti"),
    "#hair": ("barbiere", "Barbiere / tatuaggi"), "#tattoos": ("barbiere", "Barbiere / tatuaggi"),
    "#modshop": ("officina", "Officine e Pay'n'Spray"), "#pay'n'spray": ("officina", "Officine e Pay'n'Spray"),
    "#carwash": ("officina", "Officine e Pay'n'Spray"), "#bikeshop": ("officina", "Officine e Pay'n'Spray"),
    "#gas": ("benzina", "Benzinai"),
    "#supermarket": ("negozi", "Negozi"), "#electronics": ("negozi", "Negozi"), "#liquor": ("negozi", "Negozi"),
    "#pharmacy": ("negozi", "Negozi"), "#vendor": ("negozi", "Negozi"),
    "#fence": ("ricettatori", "Ricettatori"),
    "#food": ("cibo", "Cibo e locali"), "#fastfood": ("cibo", "Cibo e locali"), "#bar": ("cibo", "Cibo e locali"),
    "#drinks": ("cibo", "Cibo e locali"), "#nightclub": ("cibo", "Cibo e locali"), "#stripclub": ("cibo", "Cibo e locali"),
    "#safehouse": ("rifugi", "Rifugi"),
    "#tennis": ("attivita", "Attività"), "#golf": ("attivita", "Attività"), "#racetrack": ("attivita", "Attività"),
    "#gym": ("attivita", "Attività"), "#cinema": ("attivita", "Attività"), "#volleyball": ("attivita", "Attività"),
    "#ferriswheel": ("attivita", "Attività"), "#blimp": ("attivita", "Attività"),
    "#hospital": ("servizi", "Ospedali, polizia, prigioni"), "#police": ("servizi", "Ospedali, polizia, prigioni"),
    "#jail": ("servizi", "Ospedali, polizia, prigioni"),
    "#bus": ("trasporti", "Trasporti"), "#train": ("trasporti", "Trasporti"), "#metro": ("trasporti", "Trasporti"),
    "#metromover": ("trasporti", "Trasporti"), "#marina": ("trasporti", "Trasporti"), "#airport": ("trasporti", "Trasporti"),
    "#airbase": ("trasporti", "Trasporti"),
}
TIPO = {
    "#guns": "Armeria", "#clothes": "Abbigliamento", "#shoes": "Scarpe", "#hair": "Barbiere", "#tattoos": "Tatuaggi",
    "#modshop": "Officina tuning", "#pay'n'spray": "Pay'n'Spray", "#carwash": "Autolavaggio", "#bikeshop": "Negozio moto/bici",
    "#gas": "Benzinaio", "#supermarket": "Supermercato", "#electronics": "Elettronica", "#liquor": "Liquori",
    "#pharmacy": "Farmacia", "#vendor": "Venditore", "#fence": "Ricettatore", "#food": "Cibo", "#fastfood": "Fast food",
    "#bar": "Bar", "#drinks": "Bar", "#nightclub": "Discoteca", "#stripclub": "Strip club", "#safehouse": "Rifugio",
    "#tennis": "Tennis", "#golf": "Golf", "#racetrack": "Circuito", "#gym": "Palestra", "#cinema": "Cinema",
    "#volleyball": "Pallavolo", "#ferriswheel": "Ruota panoramica", "#blimp": "Dirigibile", "#hospital": "Ospedale",
    "#police": "Polizia", "#jail": "Prigione", "#bus": "Fermata bus", "#train": "Stazione treno", "#metro": "Metro",
    "#metromover": "Metromover", "#marina": "Porto turistico", "#airport": "Aeroporto", "#airbase": "Base aerea",
}

pois = []
search = []
for k, v in lm.items():
    if not v[1]:
        continue
    name = v[0]
    parts = [p.strip() for p in name.split(",")]
    title = parts[0] if parts[0] not in ("?", "") else None
    where = ", ".join(parts[1:])
    xy = [round(v[1][0], 1), round(v[1][1], 1)]
    tags = [t for t in v[6] if t.startswith("#")]
    if tags:
        t = tags[0]
        cat = CAT.get(t, ("attivita", "Attività"))[0]
        pois.append({"id": k, "n": title or TIPO.get(t, "Luogo"), "w": where, "t": TIPO.get(t, t[1:]), "c": cat, "p": xy})
    if title:
        search.append([title + (", " + where if where else ""), xy[0], xy[1]])

cats = []
seen = set()
for t, (c, label) in CAT.items():
    if c not in seen:
        seen.add(c); cats.append([c, label])

A = {
    "Crosstown": area("Crosstown"), "Waning Sands": area("Waning Sands"), "Capri": area("Capri"),
    "Leaf Links": area("Leaf Links"), "Shore Dr": area("Shore Dr"), "Peacock Bay": area("Peacock Bay"),
    "Ocean Beach": area("Ocean Beach"), "Rialto": area("Rialto Islands"), "La Perle": area("La Perle"),
    "Port Gellhorn": area("Port Gellhorn"), "Ambrosia": area("Ambrosia"), "Downtown": area("Downtown, Vice City"),
}

# Auto nascoste: dati da guide pubblicate a pochi giorni dall'uscita; posizioni dei pin approssimative.
S_X = "gta-xtreme.com"
S_B = "thebestmods.com"
S_S = "sportskeeda.com"
S_G = "ggwtb.com"
S_D = "detonated.com"
cars = [
    {"id": "infernus", "n": "Pegassi Infernus", "zona": "Crosstown, Vice City", "p": A["Crosstown"], "prec": "zona",
     "d": "Stazione di polizia di Crosstown su NW 9th Street: entra quando si apre il cancello del parcheggio e sali fino al livello 7. Dall'ultimo piano c'è una seconda rampa per uscire.",
     "note": "Ha il localizzatore: controllalo prima di portarla a Randy. Una fonte scrive NE 9th St, a est del Rockridge Hospital.", "src": [S_X, S_S]},
    {"id": "vitello", "n": "Pegassi Vitello", "zona": "Waning Sands", "p": A["Waning Sands"], "prec": "zona",
     "d": "Da Belville verso est fino a Waning Sands, segui Flamingo Parkway fino alla villa con il cancello. Guardando la casa dall'ingresso, è nel garage a destra più vicino alla casa.",
     "note": "Una guida indica la Clone Key per prenderla.", "src": [S_X, S_S]},
    {"id": "hellfire", "n": "Gauntlet Hellfire / Devil's Rope Gauntlet", "zona": "Hamlet, sfasciacarrozze M7", "p": at("L1570", 450, 0), "prec": "zona",
     "d": "Dal Boone Speedway vai a est lungo Galerina Street fino allo sfasciacarrozze M7. Segui il lato destro fino in fondo, vicino ai container o nel garage.",
     "note": "Le due fonti la chiamano in modo diverso; una dice che è sorvegliata da biker e che si entra dal lucernario. Apri il cancello da dentro per avere l'uscita libera.", "src": [S_X, S_B]},
    {"id": "banshee", "n": "Bravado Banshee", "zona": "Capri", "p": A["Capri"], "prec": "zona",
     "d": "Parcheggi davanti al Sweetbay Inn, su East Buckley Drive.", "note": "Vista verso le 3 di notte: se non c'è, torna di notte.", "src": [S_X]},
    {"id": "tempesta", "n": "Pegassi Tempesta", "zona": "NE 3rd Street, Vice City", "p": A["Downtown"], "prec": "zona",
     "d": "Lungo NE 3rd Street cerca un carro attrezzi con una rissa sul marciapiede; finita la lite, sgancia la Tempesta dal carro attrezzi.",
     "note": "Evento visto verso le 13. Pin messo a Downtown solo come riferimento: spostalo quando la trovi.", "src": [S_X]},
    {"id": "mamba", "n": "Mamba GT", "zona": "Leaf Links", "p": A["Leaf Links"], "prec": "zona",
     "d": "Randy ti manda alla villa di Leaf Links nella missione ¡Dale Mamba!. Dal cancello prendi il sentiero sul lato destro: l'auto è dietro l'edificio, verso la piscina.",
     "note": "La chiave è in una ciotola sul tavolo dietro il divano della casa principale (si entra con la Snap Gun).", "src": [S_X]},
    {"id": "paragon", "n": "Ascot Paragon", "zona": "Ocean Beach, Shore Drive", "p": A["Shore Dr"], "prec": "zona",
     "d": "Parcheggi davanti al Banana Hole Main Bar, lungo Shore Drive.", "note": "Vista verso le 18; se non c'è, riprova alla stessa ora un altro giorno.", "src": [S_X]},
    {"id": "furia", "n": "Piccia Furia", "zona": "Peacock Bay (Peacock Estates)", "p": A["Peacock Bay"], "prec": "zona",
     "d": "Villa con cancello su Palladia Lane: prendi il sentiero a sinistra del cancello, scavalca la siepe e passa tra l'acqua e il garage. Entra dalla porta laterale.",
     "note": "Apri la serranda prima di uscire.", "src": [S_X]},
    {"id": "toros", "n": "Pegassi Toros", "zona": "Tequesta Retreat", "p": at("L131"), "prec": "edificio",
     "d": "Posti auto davanti all'ingresso delle Pegassi Residences, su Bayside Drive.", "note": "Vista verso le 18:30.", "src": [S_X]},
    {"id": "growler", "n": "Pfister Growler", "zona": "Ocean Beach, Fig Street", "p": A["Ocean Beach"], "prec": "zona",
     "d": "Parcheggio multipiano su Fig Street: sali la rampa e controlla i posti di ogni piano.", "note": "Vista verso le 17.", "src": [S_X]},
    {"id": "penumbra", "n": "Maibatsu '97 Penumbra FF", "zona": "Vespucci Island / Neptune Circle", "p": A["Rialto"], "prec": "zona",
     "d": "Da Vice Beach verso ovest oltre il ponte delle Rialto Islands: villa grande sul lato nord della strada. Scavalca la siepe, cancelletto verde a sinistra, porta laterale accanto al garage.",
     "note": "Fonti in disaccordo sulla zona (Vespucci Island oppure Neptune Circle). Se scatta l'allarme usa il pannello sulla parete sinistra.", "src": [S_X, S_B]},
    {"id": "emerus-ruby", "n": "Royal Ruby Emerus", "zona": "Vespucci Island / Neptune Circle", "p": A["Rialto"], "prec": "zona",
     "d": "Garage di una villa sorvegliata, con guardie al cancello: aggira il cancello e scavalca la siepe.",
     "note": "Supercar con nitro. Fonti in disaccordo sulla zona.", "src": [S_B, S_D]},
    {"id": "emerus-purple", "n": "Purple Drank Emerus", "zona": "Deposito navale (da confermare)", "p": None, "prec": "nessuna",
     "d": "In un deposito navale sorvegliato.", "note": "Con nitro. Legata a un'occasione di furto nel capitolo 3. Posizione non indicata: aggiungi il pin quando la trovi.", "src": [S_B]},
    {"id": "charred-toros", "n": "Charred Toros", "zona": "La Perle, Vice City", "p": A["La Perle"], "prec": "zona",
     "d": "Nella trap house di La Perle.", "note": "Senza localizzatore, registrazione economica. Una fonte parla invece del garage di una villa.", "src": [S_B, S_D]},
    {"id": "firebug", "n": "Firebug Dominator", "zona": "Port Gellhorn, La Cascara Motel", "p": A["Port Gellhorn"], "prec": "zona",
     "d": "Al La Cascara Motel, sorvegliata dalla gang dei Kolts.", "note": "Senza localizzatore.", "src": [S_B]},
    {"id": "copperheads", "n": "Copperheads Gauntlet", "zona": "Ambrosia", "p": A["Ambrosia"], "prec": "zona",
     "d": "In un garage di Ambrosia (una fonte: edificio con l'insegna Hog Stars).", "note": "Allarme normale. Quando la prendi sblocchi una livrea.", "src": [S_B, S_D]},
    {"id": "golfer", "n": "Brimstone Golfer (golf cart in fiamme)", "zona": "Penmarch Isle", "p": None, "prec": "nessuna",
     "d": "Garage di una villa a Penmarch Isle.", "note": "Nessuna sorveglianza. Penmarch Isle non è nel database della mappa: aggiungi il pin tu.", "src": [S_B]},
    {"id": "elegy-drift", "n": "Elegy da drift / Skyline", "zona": "Gellhorn International Raceway", "p": at("L281"), "prec": "edificio",
     "d": "Nei garage del circuito: entra dalla porta laterale, passa dagli uffici e arrivi al garage.",
     "note": "Ha il localizzatore. Una fonte indica la registrazione da Moses a circa $14.000.", "src": [S_B, S_D]},
    {"id": "sanchez", "n": "Royal Sanchez", "zona": "North Mariana County, deposito container", "p": None, "prec": "nessuna",
     "d": "Container arancione nel deposito a nord di Grassrivers.", "note": "Serve l'apri-casse di Lucia (capitolo 3).", "src": [S_S, S_B, S_G]},
    {"id": "picador", "n": "Caliente Picador", "zona": "North Mariana County, deposito container", "p": None, "prec": "nessuna",
     "d": "Container giallo nello stesso deposito della Royal Sanchez.", "note": "Sposta prima gli altri container con il bulldozer.", "src": [S_S, S_B]},
    {"id": "pixel-elegy", "n": "Annis Pixel Elegy", "zona": "Capri, cantiere", "p": A["Capri"], "prec": "zona",
     "d": "Container giallo SCOOP nel Capri Construction Yard.", "note": "", "src": [S_S]},
    {"id": "jugular", "n": "Bloodless Jugular", "zona": "Leonard County", "p": None, "prec": "nessuna",
     "d": "Garage accanto a una casa bianca nella Leonard County.", "note": "Serve il Key Cloner (capitolo 3).", "src": [S_B]},
    {"id": "anarchist", "n": "Anarchist Dominator", "zona": "Parcheggio Dynamics Fitness", "p": None, "prec": "nessuna",
     "d": "Ultimo piano del parcheggio della palestra Dynamics Fitness, di giorno.", "note": "Nessuna sorveglianza.", "src": [S_G]},
    {"id": "ruiner", "n": "Turbo Ruiner", "zona": "Key Lento, vicino a casa di Jason", "p": at("L266", 250, 0), "prec": "zona",
     "d": "Casa a est della casa di Jason a Key Lento, di giorno, senza allarme.",
     "note": "Registrazione circa $6.000. ATTENZIONE: nel capitolo 1 non puoi ancora registrare le auto (Moses arriva nel capitolo 2).", "src": [S_G]},
]

# Cose da non perdere: S = fonte. "tr" = rilevante per trofei/platino.
S_W = "thegameswiki.com"
S_V = "vicemissions.com"
S_T = "gmtreks.com"
S_M = "timesaver.gg"
S_P = "promptowy.com"
chapters = [
    {"n": 1, "titolo": "Capitolo 1 (Jason, Key Lento)",
     "pnr": "Punto di non ritorno: Tourist Trap (sulla mappa «Take Up Mattia's Offer», si sblocca dopo Recalibration). Parte una serie di missioni senza giro libero che ti porta nel capitolo 2: perdi i contanti in tasca, il conto BuckMe, la scorta sotto il pavimento e la casa di Jason. Si salvano solo i Family Savings fino a $5.000. Fai un salvataggio manuale in uno slot a parte.",
     "items": [
        {"id": "c1-meditazione", "tr": True, "t": "Meditazione sul balcone di casa di Jason con Lucia",
         "d": "Dopo Down to Earth parla con Lucia finché dice che va a meditare. È uno dei 18 punti di meditazione.",
         "n": "Trofeo Positive Mental Attitude (meditare in tutti i punti). Non è confermato che serva proprio questo punto: fallo comunque.", "src": [S_W, S_M]},
        {"id": "c1-rum", "t": "Get Shirley's Rum", "d": "Missione facoltativa dopo Unwanted Attention: Shirley chiama Jason mentre va a Pipework.", "n": "Non serve per trofei né 100% (Shirley non conta per Strangers & Freaks). Dà +3% di concentrazione.", "src": [S_W, S_V, "powerpyx.com"]},
        {"id": "c1-scooter", "t": "Steal the Scooter", "d": "Si apre dopo Get Shirley's Rum.", "n": "Non serve per trofei. Dopo puoi prendere in prestito la Penumbra di Shirley.", "src": [S_W, S_V]},
        {"id": "c1-bell", "t": "Ring the Bell!", "d": "Solo all'inizio di Swamped, mentre vai al porto di Brian: dopo l'SMS di Cal vai al Rusty Anchor e riaccompagnalo a casa.", "n": "Sblocca maglietta e cappellino Rusty Anchor.", "src": [S_W]},
        {"id": "c1-droga", "t": "Find the Lost Drugs", "d": "Dopo Buck Me: quattro pacchi di cocaina nella Mariana County, circa $900 l'uno, da vendere a un ricettatore.", "n": "", "src": [S_W]},
        {"id": "c1-donnie-vendi", "t": "Vendi i narcotici a Donnie prima di Clear Skies", "d": "Il Donnie's Drop-Off chiude dopo Swamped (forse già all'inizio di Clear Skies). Donnie paga di più per i narcotici.", "n": "", "src": [S_W]},
        {"id": "c1-trailer", "t": "Contanti nel rimorchio (Gone Fishing)", "d": "Nel rimorchio bianco e rosso vicino all'uscita del campo, prima di salire sull'idrovolante.", "n": "", "src": [S_V]},
        {"id": "c1-sigari", "t": "3 sigari Macizo (Pipework)", "d": "Dopo aver riparato il lavandino di Mandy, lei butta a terra una scatola di sigari: raccoglila.", "n": "", "src": [S_W]},
        {"id": "c1-andy", "t": "Vestiti per Lucia da Andy", "d": "Proposta al telefono dopo Feng Shui, prima che inizi Coming Home.", "n": "Bonus nel rapporto con Lucia.", "src": [S_W]},
        {"id": "c1-collana", "t": "Collana per Lucia ($475)", "d": "Dopo Feng Shui, a The Siren's Chest nel sud-ovest di Key Lento.", "n": "Bonus nel rapporto con Lucia.", "src": [S_W]},
        {"id": "c1-riparazioni", "t": "4 riparazioni facoltative in casa di Jason", "d": "Spariscono dopo Coming Home.", "n": "Niente trofei, ma cambiano il rapporto con Lucia e una scena.", "src": [S_T]},
        {"id": "c1-occhiali-lucia", "t": "Occhiali da sole per Lucia (Day Release)", "d": "Mentre Lucia cerca Mattia sullo yacht, parla con la coppia vicino alla ringhiera delle scale al piano di mezzo.", "n": "", "src": [S_W]},
        {"id": "c1-donnie-occhiali", "t": "Occhiali aviator di Donnie (Don Gone)", "d": "Sulla mensola del bagno nel rimorchio di Donnie; poi li prendi dal guardaroba.", "n": "", "src": [S_W]},
        {"id": "c1-revolver", "t": "Revolver H&L .38 di Donnie (Don Gone)", "d": "Nel bagagliaio dell'auto di Donnie dopo la rissa: prendilo prima di distruggere l'auto.", "n": "Variante di arma unica.", "src": [S_W, S_V]},
        {"id": "c1-giacca", "t": "Giacca di Andy per Lucia (Home Sweet Home)", "d": "Mentre Lucia scappa dalla polizia intorno alla casa, chiama un passaggio e raggiungi l'auto senza farti vedere.", "n": "", "src": [S_W]},
        {"id": "c1-soldi", "t": "Spendi o metti al sicuro i soldi", "d": "Prima di Tourist Trap: i contanti e il conto BuckMe si perdono, i Family Savings fino a $5.000 restano.", "n": "", "src": [S_W, S_V]},
        {"id": "c1-ultimate", "t": "Moto Dinka Enduro e kayak Crest (Ultimate Edition)", "d": "Il testo del gioco dice che sono solo per il capitolo 1.", "n": "Solo Ultimate Edition.", "src": [S_W]},
        {"id": "c1-auto", "t": "Auto uniche trovate nel capitolo 1", "d": "Non puoi registrarle fino a Moses nel capitolo 2: se le lasci le perdi.", "n": "", "src": []},
     ]},
    {"n": 2, "titolo": "Capitolo 2 (Starlet Motel, Port Gellhorn)",
     "pnr": "Punto di non ritorno: Checking Out. Serve aver finito tutte le altre missioni principali del capitolo 2 e avere almeno $15.000. Quando parte perdi lo Starlet Motel come casa. Prima finisci quello che vuoi fare a Port Gellhorn.",
     "items": [
        {"id": "c2-vicki", "tr": True, "t": "Carta Vicki (set Delights Dancers)", "d": "Nel bagno dell'ufficio del motel.", "n": "Esiste una seconda copia (sotto una sedia sul tetto più alto degli appartamenti tra SW 10th Ave e SW 11th St a Southside), quindi il set non si blocca. Le carte servono per Don't Touch My Deck (3 set) e per il 100%.", "src": [S_W]},
        {"id": "c2-victor", "tr": True, "t": "Carta Victor Maravilla (set Los Santos Corkers)", "d": "Nella cucina del motel.", "n": "Seconda copia sul bordo di una panca, nel dugout di un campo da baseball sul lato ovest di Ambrosia.", "src": [S_W]},
        {"id": "c2-riviste", "t": "2 riviste nel motel", "d": "Si trovano anche altrove.", "n": "", "src": [S_W]},
     ]},
    {"n": 3, "titolo": "Capitolo 3 (appartamento a Vice City)",
     "pnr": "Nessun punto di non ritorno indicato con certezza. L'appartamento di Vice City si perde a fine capitolo.",
     "items": [
        {"id": "c3-yago", "tr": True, "t": "Race Against Yago (solo Jason)", "d": "Missione a tempo: falla appena compare.",
         "n": "La catena di Yago conta per il trofeo Strangers & Freaks: servono 8 catene e finora ne sono confermate 7, quindi non rischiare. Arriva per messaggio dopo Bumper to Bumper, con l'icona della clessidra. Il primo posto paga $3.800.", "src": ["powerpyx.com", "alcasthq.com", S_T]},
        {"id": "c3-halifax", "t": "Dubious Provenance, parti 2 e 3", "d": "Le perdi se rifiuti la statua a Halifax e poi non lo richiami.", "n": "Una fonte dice che lo scambio con Halifax scade a fine capitolo 3.", "src": [S_V, S_P]},
        {"id": "c3-riviste", "t": "2 riviste nell'appartamento", "d": "Si trovano anche altrove.", "n": "", "src": [S_W]},
     ]},
    {"n": 4, "titolo": "Capitolo 4",
     "pnr": "Punto di non ritorno (secondo una fonte): Sunset. Prima finisci i lavori secondari del capitolo 4 e prendi il biglietto alla reception dello Y Hotel.",
     "items": [
        {"id": "c4-call", "t": "This Is a Free Call From... (solo Lucia)", "d": "Missione a tempo.", "n": "Riportata come non necessaria.", "src": [S_W]},
        {"id": "c4-baddriver", "t": "Bad Driver!", "d": "Missione di Yasmani che sparisce quando inizi Power Play (si sblocca dopo Party Hard).", "n": "Yasmani non conta per Strangers & Freaks e il 100% non ha niente di perdibile: non serve al platino, ma è contenuto che perdi.", "src": [S_V, "powerpyx.com", "alcasthq.com"]},
        {"id": "c4-coppia", "t": "Attività di coppia prima di Making Gainz", "d": "Dopo Making Gainz, Jason e Lucia non possono farsi vedere insieme in pubblico fino a VCIA Takedown.", "n": "", "src": [S_V]},
        {"id": "c4-barca", "t": "Barca dell'Ultimate Edition (Washington Beach)", "d": "Usala nel capitolo 4 per sicurezza.", "n": "Non è chiaro se resti disponibile dopo.", "src": [S_W]},
     ]},
    {"n": 5, "titolo": "Capitolo 5 e finale",
     "pnr": "Punto di non ritorno: l'ufficio di Abe (Honest Abe / Protective Custody). Le ultime missioni sono di fila fino ai titoli; il gioco chiede conferma prima. Dopo il finale torni al giro libero e i contenuti secondari restano.",
     "items": [
        {"id": "c5-save", "t": "Salvataggio manuale in uno slot a parte prima dell'ufficio di Abe", "d": "", "n": "", "src": [S_V, S_T]},
     ]},
]
always = [
    {"t": "I trucchi disattivano i trofei", "d": "Se attivi un trucco i trofei sono bloccati per quella sessione: ricarica un salvataggio fatto prima del trucco.", "src": [S_T]},
    {"t": "Platino fattibile anche dopo i titoli", "d": "Il 100% (trofeo A Long Road) non ha niente di perdibile e si completa anche in giro libero dopo il finale. I trofei davvero a rischio sono due: Positive Mental Attitude (meditazione del capitolo 1) e Strangers & Freaks (Race Against Yago, a tempo).", "src": ["powerpyx.com", "alcasthq.com", S_T, S_M]},
    {"t": "Trofeo Strangers & Freaks: quali catene contano", "d": "Servono 8 catene di missioni di sconosciuti. Secondo PowerPyx contano Kirk (Skunk Ape), Kyle, Alvan, Yago, Pilot Pete, Dr. Merle (No Flushers) e Freddie; non contano Shirley, Cal, Moses, Billy, Andy, Yasmani, Tyrone, Eddie e Shayna. Per le altre (Papa Audacity, Bret, Kenton…) non si sa ancora: controlla il contatore del trofeo prima e dopo l'ultima missione di ogni catena. Con solo 7 catene sicure, quella di Yago non va persa.", "src": ["alcasthq.com", "powerpyx.com", S_T]},
    {"t": "Registrare le auto", "d": "Dal capitolo 2 (missione Moses) registri da Moses a Port Gellhorn le auto senza localizzatore; dal capitolo 3 anche ai Pay 'n' Spray quelle con localizzatore standard. Serve un posto libero in garage e Moses rifiuta le auto rubate troppo vicino alla sua officina. La prima registrazione è gratuita.", "src": ["alcasthq.com", "keengamer.com", "games.gg"]},
    {"t": "Lista di Randy", "d": "Con Clonin' Keys, Makin' Gs nel capitolo 3 sblocchi il Key Cloner e la lista di auto di Randy.", "src": [S_X]},
]

PP = "https://www.powerpyx.com/?p="
L_WALK = ("Walkthrough completo (PowerPyx)", PP + "367985")
L_WALK2 = ("Tutte le missioni in ordine (KeenGamer)", "https://www.keengamer.com/articles/guides/gta-6-walkthrough-all-chapters-and-story-missions-in-order/")
L_MISS = ("Missabili per capitolo (The Games Wiki)", "https://thegameswiki.com/gta6/wiki/missable-content-and-points-of-no-return")
L_PNR = ("Punti di non ritorno (Vice Missions)", "https://vicemissions.com/guides/points-of-no-return")
L_XT = ("Guida auto rare (GTA Xtreme)", "https://www.gta-xtreme.com/gta-6/locations/hidden-cars")
L_TBM = ("Guida auto nascoste (TheBestMods)", "https://thebestmods.com/gta-6/hidden-cars/")
L_SK = ("Auto nei container (Sportskeeda)", "https://www.sportskeeda.com/gta/all-hidden-cars-shipping-containers-gta-6-find")
L_DET = ("Auto rare e uniche (Detonated)", "https://detonated.com/gta-6-best-car-locations/")
L_GG = ("Auto rare e costi di registrazione (GGWTB)", "https://ggwtb.com/blog/gta-6-rare-cars-guide-free-locations--registration-costs-pro-routes")
L_PAT = ("Auto segrete (GTA6Pat)", "https://gta6pat.com/secrets/hidden-cars/")
L_RANDY = ("Lista di Randy (TheClick)", "https://www.theclick.gg/?p=119781")
L_KEY = ("Come avere il Key Cloner (Games.gg)", "https://games.gg/grand-theft-auto-vi/guides/grand-theft-auto-6-how-to-get-the-key-cloner/")
L_MOSES = ("Missione Moses (PowerPyx)", PP + "369759")
L_REG = ("Come registrare le auto (KeenGamer)", "https://www.keengamer.com/articles/guides/gta-vi-how-to-register-personal-cars-and-vehicles/")
L_EGG8 = ("Easter egg (Game8)", "https://game8.co/games/GTA-6/archives/638651")

links = {
    "c1-meditazione": [("Tutti i punti di meditazione (PowerPyx)", PP + "370569"), ("Meditazioni con mappa (Beebom)", "https://beebom.com/gta-6-meditation-spots-locations/")],
    "c1-rum": [("Get Shirley's Rum (PowerPyx)", PP + "372435"), ("Get Shirley's Rum (Push Square)", "https://www.pushsquare.com/guides/gta-6-get-shirleys-rum-walkthrough")],
    "c1-scooter": [("Steal the Scooter (PowerPyx)", PP + "372448"), ("Steal the Scooter (Push Square)", "https://www.pushsquare.com/guides/gta-6-steal-the-scooter-walkthrough")],
    "c1-bell": [L_MISS],
    "c1-droga": [("Find the Lost Drugs (PowerPyx)", PP + "369741"), ("Find the Lost Drugs (GTABase)", "https://www.gtabase.com/gta-6/missions/find-the-lost-drugs")],
    "c1-donnie-vendi": [L_MISS],
    "c1-trailer": [("Gone Fishing (Of Zen and Computing)", "https://www.ofzenandcomputing.com/gta-6-gone-fishing-mission-guide/"), L_PNR],
    "c1-sigari": [L_MISS],
    "c1-andy": [L_MISS],
    "c1-collana": [L_MISS],
    "c1-riparazioni": [("Trofei perdibili (GMTreks)", "https://gmtreks.com/gta6/page/01M7SFBCS2SRZR0S6355H0VN4E")],
    "c1-occhiali-lucia": [("Day Release (Beat Cop)", "https://beatcopgame.com/gta-6-day-release-mission-guide/"), L_MISS],
    "c1-donnie-occhiali": [L_MISS],
    "c1-revolver": [L_MISS, L_PNR],
    "c1-giacca": [L_MISS],
    "c1-soldi": [("Cosa perdi a fine capitolo 1 (MetaForge)", "https://metaforge.app/gta-6/gta-6-chapter-1-missables-point-of-no-return")],
    "c1-ultimate": [("Missabili del capitolo 1 (OutputLag)", "https://outputlag.com/guides/gta-6-missables/")],
    "c1-auto": [("Missabili del capitolo 1 (OutputLag)", "https://outputlag.com/guides/gta-6-missables/"), L_REG],
    "c2-vicki": [("Tutti i set di carte (PowerPyx)", PP + "372970"), ("Carte: i set e dove venderle (MetaForge)", "https://metaforge.app/gta-6/gta-6-collectible-cards-all-sets")],
    "c2-victor": [("Tutti i set di carte (PowerPyx)", PP + "372970")],
    "c2-riviste": [L_MISS],
    "c3-yago": [("Race Against Yago (PowerPyx)", PP + "369805"), ("Race Against Yago (TheClick)", "https://www.theclick.gg/?p=119775"), ("Tutti gli Strangers & Freaks (PowerPyx)", PP + "374431")],
    "c3-halifax": [("Dubious Provenance (PowerPyx)", PP + "369784"), ("Scelte con Halifax (eGamers)", "https://egamers.io/?p=130196")],
    "c3-riviste": [L_MISS],
    "c4-call": [L_MISS, L_WALK],
    "c4-baddriver": [("Bad Driver! (PowerPyx)", PP + "369829")],
    "c4-coppia": [L_PNR],
    "c4-barca": [L_MISS],
    "c5-save": [L_PNR, L_WALK2],
}
for ch in chapters:
    ch["links"] = [L_WALK, L_WALK2, L_PNR]
    for it in ch["items"]:
        it["links"] = links.get(it["id"], [])

car_links = {
    "infernus": [L_XT, L_PAT], "vitello": [L_XT, L_PAT], "hellfire": [L_XT, L_TBM], "banshee": [L_XT], "tempesta": [L_XT],
    "mamba": [L_XT, L_RANDY], "paragon": [L_XT], "furia": [L_XT], "toros": [L_XT], "growler": [L_XT],
    "penumbra": [L_XT, ("Auto da film su Vespucci Island (GTA Side)", "https://gtaside.com/tips/gta6/easter-eggs/")],
    "emerus-ruby": [L_TBM, L_DET], "emerus-purple": [L_TBM], "charred-toros": [L_TBM, L_DET], "firebug": [L_TBM],
    "copperheads": [L_TBM, L_DET], "golfer": [L_TBM], "elegy-drift": [L_TBM, L_DET], "sanchez": [L_SK, L_GG],
    "picador": [L_SK, L_GG], "pixel-elegy": [L_SK], "jugular": [L_TBM, L_KEY], "anarchist": [L_GG], "ruiner": [L_GG],
}
for c in cars:
    c["links"] = car_links.get(c["id"], [])
    if c["id"] == "penumbra":
        c["note"] = "Quasi tutte le guide la danno su Vespucci Island, in un garage, disponibile da subito; una sola dice Neptune Circle. Se scatta l'allarme usa il pannello sulla parete sinistra."
        c["src"] = [S_X, S_B, "thegta6map.com"]

L_SF = ("Tutti gli Strangers & Freaks (PowerPyx)", PP + "374431")
L_SF2 = ("Quali sconosciuti contano (AlcastHQ)", "https://alcasthq.com/?p=87611")
AL = {
 "I trucchi disattivano i trofei": [("Trofei perdibili (GMTreks)", "https://gmtreks.com/gta6/page/01M7SFBCS2SRZR0S6355H0VN4E")],
 "Platino fattibile anche dopo i titoli": [("Checklist del 100% (PowerPyx)", "https://www.powerpyx.com/gta-6-100-completion-checklist/"), ("Roadmap del platino (KeenGamer)", "https://www.keengamer.com/articles/guides/gta-6-trophy-guide-platinum-roadmap-all-55-trophies/"), ("Guida ai trofei (GMTreks)", "https://gmtreks.com/gta6/page/01M7Q14ZF65PPK5FFXSY3CJNKQ")],
 "Trofeo Strangers & Freaks: quali catene contano": [L_SF, L_SF2],
 "Registrare le auto": [L_MOSES, L_REG, ("Come tenere le auto rubate (Games.gg)", "https://games.gg/grand-theft-auto-vi/guides/how-to-keep-stolen-cars-in-grand-theft-auto-6/")],
 "Lista di Randy": [L_RANDY, L_KEY],
}
for a in always:
    a["links"] = AL[a["t"]]

S_RB = "redbull.com"; S_G8 = "game8.co"; S_GT = "gmtreks.com"; S_MF = "metaforge.app"; S_DU = "duuro.net"; S_GS = "gtaside.com"; S_TM = "thegta6map.com"
L_RB = ("Easter egg (Red Bull)", "https://www.redbull.com/int-en/gta-6-easter-eggs")
L_GTE = ("Easter egg e segreti (GMTreks)", "https://gmtreks.com/gta6/page/01M7VYV9B4MK0MZNV5A9XQVE3S")
L_MFE = ("Easter egg (MetaForge)", "https://metaforge.app/gta-6/gta-6-easter-eggs-secrets")
L_DUE = ("Easter egg (Duuro)", "https://duuro.net/blog/gta-6-easter-eggs")
L_GSE = ("Easter egg (GTA Side)", "https://gtaside.com/tips/gta6/easter-eggs/")
L_TME = ("39 segreti con mappa (TheGTA6Map)", "https://thegta6map.com/easter-eggs")
eggs = [
    {"id": "e-skunk", "n": "Skunk Ape (Bigfoot)", "zona": "Cottonmouth Lake, Grassrivers", "p": at("L3748", 0, -150), "prec": "zona",
     "d": "Dopo la prima missione vai a sud del Cottonmouth Lake e segui il sentiero: lo becchi mentre mangia un cervo. Poi c'è una catena di 3 missioni nella Mariana County.",
     "src": [S_RB, S_G8, S_MF, S_GT], "links": [L_RB, L_EGG8, L_GTE]},
    {"id": "e-ufo", "n": "Rapimento UFO", "zona": "Strada sterrata a est di Port Gellhorn", "p": at("L304", 300, 0), "prec": "zona",
     "d": "Su una strada sterrata a est di Port Gellhorn, vicino allo Starlet Motel, dopo le 2 di notte.",
     "note": "Dà un trofeo: The Truth Is Out There.", "src": [S_GT, S_RB], "links": [L_GTE, L_RB]},
    {"id": "e-vault", "n": "The Vault: stazione radio segreta", "zona": "Downtown, Vice City", "p": at("L556"), "prec": "edificio",
     "d": "Nella discoteca The Vault, a sud del Jack of Hearts e a ovest del NINE1NINE: cerca il poster rosso appena dentro l'ingresso.",
     "src": [S_RB], "links": [L_RB]},
    {"id": "e-nest", "n": "Il nido di uova di Pasqua", "zona": "In cima a un'antenna radio", "p": at("L264"), "prec": "zona",
     "d": "Arrampicati fino in cima all'antenna: c'è un nido di uova dipinte che puoi lanciare per una scena.",
     "note": "Le guide non concordano su quale antenna: a nord di Hamlet (pin), nel sud della Vice-Dale County o la torre TV più alta di Vice City.", "src": [S_DU, S_G8, S_MF, S_TM], "links": [L_DUE, L_EGG8, L_TME]},
    {"id": "e-dog", "n": "Cool Dog, il cane sulla moto d'acqua", "zona": "Mare aperto, Gambit Bay", "p": at("L3450", 600, -400), "prec": "zona",
     "d": "Vai al largo, buttati in acqua e aspetta di sentire abbaiare: il cane ti porta a una spiaggia con i suoi amici.",
     "note": "Ricompensa: un portafoglio con $1.218 e un paio di occhiali da sole.", "src": [S_RB, S_G8], "links": [L_RB, L_EGG8]},
    {"id": "e-dexter", "n": "L'appartamento di Dexter Morgan", "zona": "Trinity Apartments, Washington Island / Vice Beach", "p": None, "prec": "nessuna",
     "d": "Ai Trinity Apartments su Washington Island; sul tetto e ai moli ci sono altri due riferimenti a Dexter.",
     "note": "Un'altra guida lo mette al secondo piano di un palazzo a Vice Beach, vicino alle icone Pay'n'Spray e Top Fun Drones.", "src": [S_DU, S_MF, S_G8], "links": [L_DUE, L_MFE]},
    {"id": "e-arthur", "n": "Il cappello di Arthur Morgan (RDR2)", "zona": "Sud di Port Gellhorn", "p": None, "prec": "nessuna",
     "d": "In vendita a una svendita in giardino nel sud di Port Gellhorn.", "src": [S_MF], "links": [L_MFE]},
    {"id": "e-ritual", "n": "Il rituale demoniaco", "zona": "Nord di Capri, Tortoise Lake", "p": at("L1551"), "prec": "zona",
     "d": "Un capannone non segnato sulla mappa, vicino al Tortoise Lake: pentacolo sul pavimento con la sagoma di un corpo.", "src": [S_GS], "links": [L_GSE]},
    {"id": "e-crab", "n": "Il granchio gigante", "zona": "Pelican Valley, Gullet Marsh", "p": at("L3447"), "prec": "zona",
     "d": "In una stazione di ricerca abbandonata a Pelican Valley, nel Gullet Marsh.", "src": [S_G8], "links": [L_EGG8, L_TME]},
    {"id": "e-scarface", "n": "Villa e motel di Scarface", "zona": "Starfish Island / Ocean Beach", "p": area("Starfish Island"), "prec": "zona",
     "d": "La villa è a Starfish Island; la scena del motel è a Ocean Beach, appartamento 3C.", "src": [S_GT], "links": [L_GTE]},
    {"id": "e-epsilon", "n": "Epsilon Program", "zona": "Epsilon Center, Downtown Vice City", "p": None, "prec": "nessuna",
     "d": "Il culto di GTA V torna con un centro nel Downtown di Vice City.", "src": [S_GT], "links": [L_GTE]},
]
for e in eggs:
    e.setdefault("note", "")


# --- Missioni (elenco PowerPyx) ---
import os
HERE = os.path.dirname(os.path.abspath(__file__))
def pp_url(slug):
    return "https://www.powerpyx.com/gta-6-" + slug + ("/" if "walkthrough" in slug else "-walkthrough/")
def leonard_north():
    pts = [v[1] for v in lm.values() if v[1] and "leonard county" in v[0].lower() and v[1][1] > 4500]
    return [round(statistics.median(q[0] for q in pts)), round(statistics.median(q[1] for q in pts))]
MPIN = {
    "get-shirleys-rum": (at("L266"), "zona", "Fuori da casa di Jason, Key Lento"),
    "steal-the-scooter": (at("L266"), "zona", "Fuori da casa di Jason, Key Lento"),
    "find-the-lost-drugs": (at("L3447"), "zona", "Paludi della Mariana County (4 zone di ricerca)"),
    "day-release-meet-mattia-kat": (at("L325"), "edificio", "The Rusty Anchor, Key Lento"),
    "moses-take-a-vehicle-to-moses": (A["Port Gellhorn"], "zona", "Officina di Moses, Port Gellhorn"),
    "daily-driver-steal-the-crawler-for-moses": (A["Port Gellhorn"], "zona", "Port Gellhorn"),
    "check-out-mckittrick-farm": (at("L304"), "edificio", "Volantino di Kyle fuori dallo Starlet Motel"),
    "gellhorns-missing-tourists": (at("L304", -60, 0), "edificio", "Manifesto nell'ufficio dello Starlet Motel (altri a Port Gellhorn)"),
    "race-against-yago": (area("Salton, Vice City"), "zona", "Salton, Vice City"),
    "bad-driver-find-felipe": (area("Millport"), "zona", "Millport, Lummox County"),
    "the-last-mile-passing-the-torch-recover-petes-plane": (at("L1566"), "edificio", "Sundown Private Airfield"),
    "the-final-flush-meet-at-franks-waffles": (area("Tequesta"), "zona", "Tequesta, Vice City (Frank's Waffles)"),
    "retest-freddies-defenses": (leonard_north(), "zona", "Nord della Leonard County, complesso di Freddie"),
    "the-unknown-stuntman": (A["Ocean Beach"], "zona", "Ocean Beach, Vice Beach"),
    "veteran-hunted-meet-bret": (area("Lummox County"), "zona", "Lummox County (solo Jason)"),
    "search-for-the-skunk-ape": (at("L3748"), "zona", "Parte da un volantino di Kirk; lo Skunk Ape è intorno al Cottonmouth Lake"),
    "dubious-provenance-visit-the-antique-store": (A["Capri"], "zona", "Negozio di antiquariato a Capri"),
}
def parse(path):
    out, cur = [], None
    for line in open(os.path.join(HERE, path), encoding="utf-8"):
        line = line.rstrip("\n")
        if not line: continue
        if line.startswith("#"):
            cur = {"h": line[1:].split("|"), "m": []}; out.append(cur); continue
        parts = line.split("|")
        cur["m"].append({"n": parts[0], "id": parts[1], "f": (parts[2].split(",") if len(parts) > 2 else [])})
    return out
mission_ch = []
for sec in parse("missions_src.txt"):
    mission_ch.append({"n": int(sec["h"][0]), "t": sec["h"][1], "m": sec["m"]})
sf = []
for sec in parse("sf_src.txt"):
    sf.append({"g": sec["h"][0], "ch": int(sec["h"][1]), "conta": sec["h"][2], "m": sec["m"]})
mdb = {}
for ch in mission_ch:
    for m in ch["m"]:
        mdb[m["id"]] = {"n": m["n"], "ch": ch["n"]}
for g in sf:
    for m in g["m"]:
        mdb.setdefault(m["id"], {"n": m["n"], "ch": g["ch"]})
for k, v in mdb.items():
    v["u"] = pp_url(k)
    if k in MPIN:
        pnt, prec, where = MPIN[k]; v["p"] = pnt; v["prec"] = prec; v["w"] = where
missing = [k for k in MPIN if k not in mdb]
assert not missing, missing

# --- Sblocco per capitolo (verificato su guide/wiki) ---
POI_GATE = {
    "L266": (1, 1, "Rifugio solo nel capitolo 1"),
    "L304": (2, 2, "Rifugio solo nel capitolo 2 (fino a Checking Out)"),
    "L475": (3, 3, "Probabile rifugio del capitolo 3 a Vice City (non confermato)"),
    "L16": (4, None, "Probabile base del capitolo 4 (non confermato)"),
    "L348": (2, None, "Officina di Moses: registrazione auto, Slim Jim e vendita auto dal capitolo 2"),
    "L286": (2, None, "Ricettatori di Port Gellhorn: dal capitolo 2"),
    "L1104": (2, None, "Ricettatori di Port Gellhorn: dal capitolo 2"),
    "L539": (3, None, "Ricettatori di Vice City: dal capitolo 3"),
    "L910": (3, None, "Ricettatori di Vice City: dal capitolo 3"),
    "L1009": (3, None, "Ricettatori di Vice City: dal capitolo 3"),
    "L1117": (1, None, "Quando si sblocchi non è verificato"),
    "L415": (1, None, "Riverniciatura da subito; vendita e registrazione di auto con localizzatore dal capitolo 3"),
}
for p_ in pois:
    g = POI_GATE.get(p_["id"])
    if g:
        p_["ch"], p_["to"], p_["g"] = g
    if p_["id"] == "L348":
        p_["n"] = "Officina di Moses (Watkins Auto Parts)"
CAR_GATE = {
    "infernus": (3, "Va consegnata a Randy: la sua lista si apre nel capitolo 3"),
    "vitello": (3, "Serve il Key Cloner (capitolo 3, Clonin' Keys, Makin' GS)"),
    "mamba": (3, "È nella missione di Randy ¡Dale Mamba! (capitolo 3)"),
    "jugular": (3, "Serve il Key Cloner (capitolo 3)"),
    "sanchez": (3, "Serve il Cut-Off Tool (capitolo 3, Meet the Heders)"),
    "picador": (3, "I container gialli Scoop si aprono solo con la smerigliatrice (capitolo 3, Meet the Heders)"),
    "pixel-elegy": (3, "I container gialli Scoop si aprono solo con la smerigliatrice (capitolo 3, Meet the Heders)"),
    "emerus-purple": (3, "Legata a un furto del capitolo 3"),
}
CAR_GATE["elegy-drift"] = (3, "Ha il localizzatore: si registra ai Pay 'n' Spray dal capitolo 3")
for c in cars:
    g = CAR_GATE.get(c["id"])
    c["ch"], c["g"] = (g if g else (2, "Si registrano da Moses dal capitolo 2: nel capitolo 1 puoi guidarle ma non tenerle"))
# voci dei capitoli collegate alle missioni: una sola spunta
ITEM_MIS = {"c1-rum": "get-shirleys-rum", "c1-scooter": "steal-the-scooter", "c1-droga": "find-the-lost-drugs",
            "c1-andy": "get-lucias-clothes", "c1-collana": "buy-lucia-a-necklace", "c3-yago": "race-against-yago",
            "c4-baddriver": "bad-driver-find-felipe", "c4-call": "this-is-a-free-call-from-pick-up-shayna"}
for ch in chapters:
    for it in ch["items"]:
        if it["id"] in ITEM_MIS: it["mis"] = ITEM_MIS[it["id"]]
for e in eggs:
    e["ch"] = 1
S_NE = "nerdism.com"; S_S4 = "space4games.com"; S_BB = "beebom.com"; S_GU = "gamersuniverse.eu"; S_GW = "gta.wiki"; S_BX = "bloxodes.com"
L_NE = ("Cosa si sblocca e quando (Nerdism)", "https://nerdism.com/gta-6-progress-guide-what-unlocks-when/")
L_S4 = ("Strumenti e quando li ottieni (Space4Games)", "https://space4games.com/en/games-en/gta-6-gadgets-tools-unlock-guide/")
L_BB = ("Tutti i ricettatori (Beebom)", "https://beebom.com/gta-6-fence-locations/")
L_EQ = ("Le 12 attrezzature (TheClick)", "https://www.theclick.gg/gta-6-equipment-list/")
unlocks = {
 1: [
  {"t": "Mappa tutta esplorabile", "d": "Puoi girare tutta Leonida da subito, ma la storia resta nelle Leonida Keys per circa il primo 30%.", "src": ["fanboydestroy.com", "yahoo.com"], "links": [("Perché le Keys ti tengono lì (FanboyDestroy)", "https://fanboydestroy.com/games/gta-6-leonida-map-keys-early-game-limitation/")]},
  {"t": "Prima arma e Ammu-Nation", "d": "Gear Up ti dà la prima pistola; le armerie vendono armi, giubbotti e munizioni.", "src": [S_NE], "links": [L_NE]},
  {"t": "Conto BuckMe", "d": "Con Buck Me apri il conto in banca; sopra i $1.000 si paga dall'app.", "src": [S_NE], "links": [L_NE]},
  {"t": "Attrezzi del capitolo 1", "d": "Binocolo (Gone Fishing), scanner della polizia (Unwanted Attention), metal detector per i dobloni (Island Dreams), app WAiNK per scansionare le auto.", "src": [S_S4], "links": [L_S4, L_EQ]},
  {"t": "Ricettatori: Brian e Donnie", "d": "Brian (sud di Key Lento) dopo Lab Fees, fino a fine capitolo; Donnie (rimorchio nel nord di Key Lento) fino a Swamped.", "src": [S_BB, "thegameswiki.com"], "links": [L_BB]},
  {"t": "Carte collezionabili", "d": "Si possono raccogliere dopo Gone Fishing.", "src": [S_GW], "links": [("Set di carte (gta.wiki)", "https://gta.wiki/w/Collectible_Card_Sets")]},
  {"t": "Auto: guidi tutto, tieni solo quella di Jason", "d": "Puoi rubare qualsiasi auto, ma non puoi ancora registrarla.", "src": [S_NE, "alcasthq.com"], "links": [L_REG]},
 ],
 2: [
  {"t": "Moses: registrazione auto e Slim Jim", "d": "Con la missione Moses registri le auto senza localizzatore (la prima è gratis), ricevi lo Slim Jim per aprirle senza allarme e l'app Scooter Bros che ti porta l'auto.", "src": [S_NE, "pcgamer.com"], "links": [L_MOSES, L_NE]},
  {"t": "Garage in vendita", "d": "Dopo Daily Driver l'app Vice City Real Estate vende 8 garage (da $4.000 a $40.000). Sono l'unica proprietà acquistabile.", "src": [S_BX, S_GU], "links": [("Si possono comprare case? (Bloxodes)", "https://bloxodes.com/articles/gta-6-can-you-buy-houses")]},
  {"t": "Cambio libero Jason/Lucia", "d": "Dopo Coffee Break puoi passare da un personaggio all'altro in giro libero.", "src": [S_GU, "powerpyx.com"], "links": []},
  {"t": "Ricettatori di Port Gellhorn", "d": "Moses (auto) e il rimorchio di Dunk.", "src": [S_BB], "links": [L_BB]},
  {"t": "Altri attrezzi", "d": "Piede di porco (in un covo dei Kolt & Associates).", "src": [S_S4], "links": [L_S4]},
 ],
 3: [
  {"t": "Pay 'n' Spray per le auto con localizzatore", "d": "In ogni Pay 'n' Spray vendi le auto rubate e registri quelle con localizzatore standard.", "src": [S_NE, S_BX], "links": [L_NE]},
  {"t": "Key Cloner e lista di Randy", "d": "Clonin' Keys, Makin' GS ti dà il Key Cloner per le auto senza chiave e apre la lista di Randy (circa $30.000 a consegna).", "src": [S_NE, "theclick.gg"], "links": [L_KEY, L_RANDY]},
  {"t": "Yasmani: gioiellerie e Snap Gun", "d": "Colpi alle gioiellerie e Snap Gun per aprire le porte in silenzio (l'allarme resta attivo). Da Yasmani puoi anche scegliere il ricettatore dal garage.", "src": [S_NE, "pcgamer.com", S_BB], "links": [L_NE]},
  {"t": "Attrezzi per container e casse", "d": "Meet the Heders: pry bar, Cut-Off Tool e smerigliatrice (apre i container gialli Scoop). Credit Check: Dye Pack Jammer per vendere le banconote segnate.", "src": [S_S4, "theclick.gg", "xboxplay.games", S_BX], "links": [L_S4, L_EQ]},
  {"t": "Rapine a prestiti e banche", "d": "Payday loans e banche (banconote segnate) si sbloccano nel capitolo 3.", "src": ["powerpyx.com"], "links": [("Tutti i ricettatori (PowerPyx)", PP + "370548")]},
 ],
 4: [
  {"t": "Caveau delle banche", "d": "Si aprono con la missione facoltativa That's Where The Money Is, verso la fine del capitolo 4 (una fonte dice capitolo 5). Un caveau grande vale fino a $205.000 e ti dà subito 4 stelle.", "src": [S_NE, "metaforge.app", "powerpyx.com"], "links": [L_NE]},
  {"t": "Furgoni portavalori", "d": "Yasmani ti dà le soffiate dopo la missione dei caveau.", "src": [S_NE], "links": [L_NE]},
 ],
 5: [
  {"t": "Dopo il finale", "d": "Giro libero, trucchi (disattivano i trofei nella sessione) e la checklist del 100% in Progressi → Statistiche.", "src": [S_NE, "gmtreks.com"], "links": [L_NE]},
 ],
}

import sys as _sys
_sys.path.insert(0, HERE)
import trophies as _tro
TRO = _tro.build(None, at)

from missions_it import it_name
import re as _re
for k, v in mdb.items():
    t = it_name(k)
    if t: v["it"] = t
# nomi inglesi nelle descrizioni -> titolo italiano
_SKIP = {"Moses", "Sunset", "Ocean Beach", "Peach!", "Check Out", "Power Play", "Team Building", "Safe Word", "Cooties", "Slam Dunk", "Feng Shui", "Island Dreams", "Crosstown Traffic", "VC Baby", "Doggie Bag"}
_pairs = {}
for k, v in mdb.items():
    if not v.get("it"): continue
    base = _re.split(r" \(| – ", v["n"])[0].strip()
    if base in _SKIP or len(base) < 6 or base == v["it"]: continue
    _pairs[base] = v["it"]
_pairs.update({"Gear Up": "Armi in spalla", "Buck Me": "Tasche Buckate", "That's Where The Money Is": "Il profumo dei soldi", "Clonin' Keys, Makin' GS": "Chiavi clonate, soldi a palate", "Clonin' Keys, Makin' Gs": "Chiavi clonate, soldi a palate"})
_rx = _re.compile(r"(«?)\b(" + "|".join(_re.escape(b) for b in sorted(_pairs, key=len, reverse=True)) + r")(?![\w'])(»?)")
def _it(s):
    r = _it0(s)
    if r.startswith("«") and r.endswith("»") and r.count("«") == 1 and s != r: r = r[1:-1]
    return r
def _it0(s):
    return _rx.sub(lambda m: (m.group(1) + _pairs[m.group(2)] + m.group(3)) if m.group(1) else "«" + _pairs[m.group(2)] + "»" + m.group(3), s)
def _walk(o, key=None):
    if isinstance(o, tuple): o = list(o)
    if isinstance(o, str): return o if key in ("n", "u", "id", "url") else _it(o)
    if isinstance(o, list): return [o[0] if (len(o) == 2 and isinstance(o[1], str) and o[1].startswith("http") and i == 1) else _walk(x, key) for i, x in enumerate(o)] if not (len(o) == 2 and all(isinstance(x, str) for x in o) and o[1].startswith("http")) else [_it(o[0]), o[1]]
    if isinstance(o, dict): return {k: _walk(v, k) for k, v in o.items()}
    return o
chapters = _walk(chapters); always = _walk(always); unlocks = {k: _walk(v) for k, v in unlocks.items()}; cars = _walk(cars); eggs = _walk(eggs)
from anchors import anchors as _anchors
for _c in chapters:
    for _i in _c["items"]:
        if "Ultimate Edition" in _i["t"]: _i["ue"] = True
_A = _anchors(chapters, mission_ch, mdb)
for _c in chapters:
    for _i in _c["items"]:
        s, p = _A.get(_i["id"], (None, "any")); _i["at"] = s or ""; _i["pos"] = p
for t in TRO["trophies"]:
    t["tip"] = t["tip"].replace("scheda Missioni", "scheda Storia")
    for f in ("d", "tip"): t[f] = _it(t[f])
    if t.get("links"): t["links"] = _walk(t["links"])
for h in TRO["hundred"]: h["n"] = _it(h["n"])
data = {"tro": TRO, "unlocks": unlocks, "missions": {"ch": mission_ch, "sf": sf, "db": mdb}, "cats": cats, "pois": pois, "cars": cars, "chapters": chapters, "always": always, "eggs": eggs, "search": search}
json.dump(data, open(out, "w"), ensure_ascii=False, separators=(",", ":"))
print(len(pois), len(search), len(cars), sum(len(c["items"]) for c in chapters))
print({k: v for k, v in A.items()})
