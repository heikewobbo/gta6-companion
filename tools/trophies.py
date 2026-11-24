# Trofei (GTABase), checklist 100% (PowerPyx), operazioni illegali (PowerPyx), guide collezionabili.
PX = "https://www.powerpyx.com/"
G = lambda slug: PX + "gta-6-" + slug + "/"

GUIDES = {
    "meditazioni": ("Meditazioni (PowerPyx)", G("all-meditation-spot-locations")),
    "carte": ("Set di carte (PowerPyx)", G("all-collectible-card-sets-locations")),
    "waink": ("Scansioni WAiNK (PowerPyx)", G("all-waink-scan-locations")),
    "stunt": ("Salti acrobatici (PowerPyx)", G("all-stunt-jump-locations")),
    "knife": ("Knife Flight (PowerPyx)", G("all-knife-flight-locations")),
    "base": ("Base jump (PowerPyx)", G("all-base-jump-locations")),
    "shoot": ("Poligoni, medaglie d'oro (PowerPyx)", G("all-shooting-range-gold-medal-challenges")),
    "drone": ("Gare e time trial dei droni (PowerPyx)", G("all-top-fun-drone-race-time-trial-locations")),
    "races": ("Gare uniche (PowerPyx)", G("all-unique-race-locations-racing-activities")),
    "racech": ("Sfide di gara, medaglie d'oro (PowerPyx)", G("all-race-challenge-locations-gold-medals")),
    "challenges": ("Le 80 sfide (PowerPyx)", G("all-challenges-guide")),
    "gangops": ("Operazioni illegali (PowerPyx)", G("all-illegal-gang-operations-locations")),
    "banks": ("Banche e caveau (PowerPyx)", G("all-bank-jobs-locations-bank-vaults")),
    "payday": ("Payday loans (PowerPyx)", G("all-payday-loans-jobs-locations")),
    "smash": ("Smash 'N' Grab (PowerPyx)", G("all-smash-n-grabs-locations")),
    "magazines": ("Riviste, libri e fumetti (PowerPyx)", G("all-magazines-books-comics-locations")),
    "bookswap": ("Book swap (PowerPyx)", G("all-book-swap-locations")),
    "flamingos": ("Fenicotteri di cocaina (PowerPyx)", G("all-cocaine-flamingo-locations")),
    "playlists": ("Playlist uniche (PowerPyx)", G("all-unique-playlist-collectible-locations")),
    "videogames": ("Videogiochi (PowerPyx)", G("all-video-game-locations")),
    "pool": ("Avversari a biliardo (PowerPyx)", G("all-pool-opponent-locations")),
    "golf": ("Minigolf e golf (PowerPyx)", G("all-golf-course-locations")),
    "hoops": ("Canestri (PowerPyx)", G("all-basketball-hoop-locations")),
    "fences": ("Ricettatori (PowerPyx)", PX + "?p=370548"),
    "sf": ("Strangers & Freaks (PowerPyx)", PX + "?p=374431"),
    "hundred": ("Checklist del 100% (PowerPyx)", G("100-completion-checklist")),
    "trophyguide": ("Guida ai trofei (GTABase)", "https://www.gtabase.com/articles/gta-6/gta-6-achievements-trophies-list-ps5-xbox-series"),
    "effigies": ("Effigi sugli alberi (PowerPyx)", G("search-for-tree-effigies-locations-walkthrough")),
    "kitty": ("Laboratori Kitty Litter (PowerPyx)", G("all-kitty-litter-lab-locations")),
}

# Contatori condivisi tra trofei e 100% (chiave -> etichetta, totale nel gioco)
COUNTERS = {
    "stunts": ("Acrobazie", 397), "meditazioni": ("Meditazioni", 18), "carte": ("Set di carte completi", 18),
    "waink": ("Luoghi WAiNK scansionati", None), "shoot": ("Ori ai poligoni", 42), "dronewins": ("Gare droni vinte (località)", 14),
    "droneTT": ("Time trial droni", 42), "races": ("Gare uniche vinte", 40), "challenges": ("Sfide completate", 80),
    "vehicles": ("Veicoli scansionati", 277), "animals": ("Animali studiati", 255), "vaults": ("Caveau rapinati", 8),
    "bills": ("Banconote segnate vendute ($)", None), "spent": ("Spesi nei negozi ($)", None), "garages": ("Garage comprati", 8),
    "registered": ("Veicoli registrati", None), "randy": ("Auto consegnate a Randy", 16), "tasks": ("Attività facoltative", None),
    "banks": ("Colpi in banca completi", 22), "payday": ("Payday loans completi", 7), "smash": ("Smash 'N' Grab completi", 35),
    "stickups": ("Rapine a mano armata completate", 91), "narcotics": ("Narcotici venduti ($)", None), "jewelry": ("Gioielli venduti ($)", None),
    "vehfenced": ("Veicoli venduti ($)", None), "kenton": ("Set di Kenton", 7), "underwater": ("Scoperte subacquee", 33),
    "magazines": ("Riviste, libri e fumetti", 34), "flamingos": ("Fenicotteri distrutti", 125), "playlists": ("Playlist uniche", 2),
    "styles": ("Stili scoperti", 79), "racech": ("Ori nelle sfide di gara", 13), "videogames": ("Videogiochi giocati", 4),
    "pool": ("Avversari di biliardo battuti", 7), "golf": ("Minigolf giocati", 3), "hoops": ("Canestri", 100),
    "bret": ("Mazzi di caccia di Bret", 15), "weapons": ("Armi standard trovate", 66),
}

# name, grade, hidden, desc (it), tip (it), chapter, counter (key, target) or mission slug or computed
TROPHIES = [
    ("Vice Got a Price!", "P", 0, "Congratulazioni! Sei una leggenda di Leonida.", "Si sblocca con tutti gli altri trofei.", 1, None),
    ("Just Like Paradise", "B", 1, "Completa Gone Fishing.", "Trofeo della storia, all'inizio del capitolo 1.", 1, {"mis": "gone-fishing"}),
    ("Paradise Lost", "B", 1, "Completa il capitolo 1.", "Arriva con la prima missione del capitolo 2.", 1, {"mis": "discharge-time"}),
    ("T**s Ass Drug Money", "B", 1, "Completa il capitolo 2.", "Arriva all'inizio del capitolo 3.", 2, {"mis": "checking-out-move-to-vice-city"}),
    ("Vice City, Baby!", "B", 1, "Completa il capitolo 3.", "Arriva dopo le prime due missioni del capitolo 4.", 3, {"mis": "the-cartel-heist"}),
    ("Top Of The World, Ma", "B", 1, "Completa il capitolo 4.", "Trofeo della storia, non si può perdere.", 4, {"mis": "starting-from-zero"}),
    ("You Gotta Know When to Get Off", "G", 1, "Completa la missione finale.", "Finisci l'ultima missione della storia.", 5, {"mis": "the-end-of-the-road"}),
    ("Trust", "B", 1, "Completa Breakfast Run.", "Missione del capitolo 2.", 2, {"mis": "breakfast-run-check-on-jason"}),
    ("Break the Bank", "B", 1, "Completa The Cartel Heist.", "Missione del capitolo 3.", 3, {"mis": "the-cartel-heist"}),
    ("Family Matters", "B", 1, "Completa Child's Play.", "Missione del capitolo 4.", 4, {"mis": "childs-play-rescue-rafa-from-kidnappers"}),
    ("DWNFALL", "B", 1, "Completa Headliners.", "Missione del capitolo 4.", 4, {"mis": "headliners-help-with-the-launch-party"}),
    ("Hi-Jacked", "B", 1, "Completa VCIA Takedown.", "Missione del capitolo 4.", 4, {"mis": "vcia-takedown"}),
    ("Snow Storm", "B", 1, "Completa Operation Savage Glory.", "Missione del capitolo 5.", 5, {"mis": "operation-savage-glory"}),
    ("A Long Road", "G", 0, "Raggiungi il 100% di completamento.", "Il più lungo: completa la checklist del 100% (si vede dopo la storia).", 1, {"calc": "hundred"}),
    ("Cunning Stunts", "S", 0, "Completa 250 acrobazie.", "Valgono tutte; passare sotto i ponti in aereo è il modo più rapido.", 1, {"cnt": "stunts", "t": 250}),
    ("Master of None", "B", 0, "Prova ogni tipo di attività una volta.", "Prova una volta tutti e nove i tipi di attività.", 1, None),
    ("The Shootist", "S", 0, "Ottieni l'oro in tutte le sfide dei poligoni.", "Oro in tutte le sfide dei 12 poligoni (serve un Waiver Pass da $5).", 1, {"cnt": "shoot", "t": 42}),
    ("Top Fun", "B", 0, "Vinci una gara di droni Top Fun in ogni località.", "Una vittoria in ciascuna delle 14 località.", 1, {"cnt": "dronewins", "t": 14}),
    ("Earn Cash, Not Kudos", "B", 0, "Vinci 20 gare diverse.", "Rivincere la stessa gara non conta.", 1, {"cnt": "races", "t": 20}),
    ("Baited My Tackle", "B", 0, "Batti Cal in una sfida di pesca.", "Con le missioni di pesca di Cal, dopo il capitolo 1.", 2, {"mis": "catch-a-bigger-fish"}),
    ("Stick Fiddler", "B", 0, "Completa un videogioco arcade.", "Arriva alla fine di un qualsiasi gioco arcade.", 1, None),
    ("Road to Rehabilitation", "B", 1, "Completa l'ultima missione per Andy.", "Cinque missioni solo con Lucia, dal capitolo 3.", 3, {"mis": "puff-puff-pass-meet-at-the-warehouse"}),
    ("This Was No Boat Accident", "B", 1, "Completa l'ultima missione per Kenton.", "Recupera i tesori dei sette relitti.", 1, {"cnt": "kenton", "t": 7}),
    ("The Lone Rider", "B", 1, "Completa l'ultima missione per Billy.", "Cinque lavori che partono dal mud club della Kelly County.", 2, {"mis": "hometown-heroes"}),
    ("Strangers & Freaks", "S", 0, "Completa 8 catene di missioni per sconosciuti in tutta Leonida.", "Servono 8 catene che contano: vedi la lista Strangers & Freaks nella scheda Missioni.", 1, {"calc": "sf"}),
    ("Supply & Demand", "B", 1, "Completa l'ultima missione per Randy.", "Consegna 16 auto sportive al suo garage.", 3, {"cnt": "randy", "t": 16}),
    ("Spin On This!", "B", 1, "Completa l'ultima missione per Tyrone.", "Solo Jason: distruggi i laboratori di droga sintetica.", 3, {"mis": "spin-on-this-shut-down-the-labs"}),
    ("Positive Mental Attitude", "B", 0, "Medita in tutti i punti di Leonida.", "Tutte e 18 le meditazioni; quella del capitolo 1 forse si perde.", 1, {"cnt": "meditazioni", "t": 18}),
    ("Fair Game", "B", 1, "Caccia un animale unico per Bret.", "Caccia gli animali dei mazzi di Bret; quale animale lo sblocchi non è confermato.", 2, None),
    ("Don't Touch My Deck", "S", 0, "Completa 3 set di carte collezionabili.", "Tre set qualsiasi; i più piccoli sono Backyard Wrestling e Delights Dancers.", 1, {"cnt": "carte", "t": 3}),
    ("You WAiNKer!", "S", 0, "Usa WAiNK It in 100 luoghi.", "Scansiona 100 punti WAiNK con l'app.", 1, {"cnt": "waink", "t": 100}),
    ("One Last Thing", "B", 0, "Completa 50 sfide.", "50 delle 80 sfide.", 1, {"cnt": "challenges", "t": 50}),
    ("Hot Together", "B", 0, "Seminate 4 stelle insieme al partner e uscite dalla zona calda.", "Prendi 4 stelle col partner, poi esci dalla zona di ricerca.", 1, None),
    ("Retail Therapy", "B", 0, "Rapina 3 negozi di fila col partner senza perdere il livello di ricercato.", "Tre negozi di fila mentre sei ancora ricercato.", 1, None),
    ("Whip It Good", "B", 0, "Scopri 100 veicoli.", "Scansiona 100 veicoli diversi, non serve guidarli.", 1, {"cnt": "vehicles", "t": 100}),
    ("Gunslinger", "B", 0, "Abbatti 5 nemici con un solo uso del Combat Focus.", "Riempi il Focus e abbattine cinque in un solo uso.", 1, None),
    ("Catch Me If You Can", "B", 1, "Fai una partenza fuori programma al VCIA.", "Ruba un aereo di linea da un gate e decolla.", 1, None),
    ("Challenging Tank", "B", 1, "Fa un po' caldo in questi Rhino.", "Ruba un carro armato alla Mile Zero Air Station e combatti da lì.", 1, None),
    ("Sneakthief", "B", 0, "Rapina una gioielleria senza farti scoprire.", "Snap Gun sulla porta sul retro e svuota la cassaforte in silenzio.", 3, None),
    ("Maximum Withdrawal", "S", 0, "Rapina 5 caveau e scappa.", "Cinque caveau, dopo la missione facoltativa del capitolo 4.", 4, {"cnt": "vaults", "t": 5}),
    ("A Classic Blitz Play", "B", 0, "Rapina un furgone portavalori e scappa.", "Apri le porte posteriori con una bomba adesiva, poi scappa.", 4, None),
    ("The Goodtime State", "B", 0, "Esplora tutta Leonida.", "Togli tutta la nebbia dalla mappa, in aereo fai prima.", 1, None),
    ("Pest Control", "B", 0, "Rapina un'operazione illegale di ogni gang.", "Una per ciascuna delle nove gang: vedi la lista Rapine.", 1, {"calc": "pest"}),
    ("In The Beginning…", "B", 1, "Goditi un cocktail con vista su Ocean Beach.", "Passaggi non confermati.", 1, None),
    ("Capital Offense", "B", 1, "Esci sfondando da un salone d'auto, in stile classico.", "Passaggi non confermati: probabilmente uscire in auto dalla vetrina.", 1, None),
    ("Let's Go Bowling", "B", 1, "Vai fino in fondo al bowling dei Kolt & Associates.", "Prendi i tre oggetti di valore al Kingpin Bowling e semina la polizia.", 2, None),
    ("Personal Best", "B", 1, "Una collaborazione di massa.", "Forza al massimo per entrambi i personaggi nelle palestre.", 1, None),
    ("Actions Speak Louder", "B", 1, "Scelte fatte (nel bene o nel male).", "500 azioni che cambiano il profilo criminale; evita il profilo Irredeemable, che è permanente.", 1, None),
    ("Bad Luck, I Guess", "B", 1, "Al secondo tentativo va meglio.", "Passaggi non confermati.", 1, None),
    ("The Truth Is Out There", "B", 1, "Cosa diavolo è appena successo?", "Il rapimento UFO a est di Port Gellhorn, dopo le 2 di notte (vedi Segreti).", 1, None),
    ("Ten Pin", "B", 1, "Abbattili con un drive-by corpo a corpo.", "Passaggi non confermati.", 1, None),
    ("Dime on the Dollar", "B", 0, "Guadagna $250.000 riciclando banconote segnate coi tuoi contatti.", "Vendi ai ricettatori le banconote segnate delle rapine (serve il Dye Pack Jammer).", 3, {"cnt": "bills", "t": 250000}),
    ("Treat Yo Self", "B", 0, "Spendi $100.000 nei negozi.", "Armi, modifiche alle auto e tatuaggi fanno salire in fretta.", 1, {"cnt": "spent", "t": 100000}),
    ("Little Boxes", "B", 0, "Compra tutti i garage.", "Gli otto garage dell'app Vice City Real Estate.", 2, {"cnt": "garages", "t": 8}),
    ("On the Spot", "B", 0, "Registra 10 veicoli sull'app Scooter Bros.", "Registra auto rubate da Moses.", 2, {"cnt": "registered", "t": 10}),
]
TROPHY_LINKS = {
    "Cunning Stunts": ["stunt", "knife", "base"], "The Shootist": ["shoot"], "Top Fun": ["drone"], "Earn Cash, Not Kudos": ["races"],
    "Positive Mental Attitude": ["meditazioni"], "Don't Touch My Deck": ["carte"], "You WAiNKer!": ["waink"], "One Last Thing": ["challenges"],
    "Maximum Withdrawal": ["banks"], "Pest Control": ["gangops"], "A Long Road": ["hundred"], "Strangers & Freaks": ["sf"],
    "Dime on the Dollar": ["fences"], "Spin On This!": ["kitty"], "Stick Fiddler": ["videogames"],
}

# 100%: (sezione, requisito, chiave contatore o calc, obiettivo, guide)
HUNDRED = [
    ("Storia e attività", "Finisci la storia", {"mis": "the-end-of-the-road"}, 1, []),
    ("Storia e attività", "Attività facoltative completate", {"cnt": "tasks"}, 100, []),
    ("Storia e attività", "Operazioni delle gang ripulite", {"calc": "gangops"}, 39, ["gangops"]),
    ("Storia e attività", "Colpi in banca completi", {"cnt": "banks"}, 22, ["banks"]),
    ("Storia e attività", "Payday loans completi", {"cnt": "payday"}, 7, ["payday"]),
    ("Storia e attività", "Smash 'N' Grab completi", {"cnt": "smash"}, 34, ["smash"]),
    ("Storia e attività", "Rapine a mano armata", {"cnt": "stickups"}, 50, []),
    ("Storia e attività", "Narcotici venduti ($)", {"cnt": "narcotics"}, 100000, ["fences"]),
    ("Storia e attività", "Gioielli venduti ($)", {"cnt": "jewelry"}, 100000, ["fences"]),
    ("Storia e attività", "Banconote segnate vendute ($)", {"cnt": "bills"}, 250000, ["fences"]),
    ("Storia e attività", "Caveau rapinati", {"cnt": "vaults"}, 8, ["banks"]),
    ("Storia e attività", "Veicoli venduti ($)", {"cnt": "vehfenced"}, 200000, []),
    ("Esplorazione e attività", "Set di Kenton", {"cnt": "kenton"}, 5, []),
    ("Esplorazione e attività", "Set di carte completi", {"cnt": "carte"}, 15, ["carte"]),
    ("Esplorazione e attività", "Luoghi WAiNK scansionati", {"cnt": "waink"}, 100, ["waink"]),
    ("Esplorazione e attività", "Scoperte subacquee", {"cnt": "underwater"}, 33, []),
    ("Esplorazione e attività", "Riviste, libri e fumetti", {"cnt": "magazines"}, 30, ["magazines", "bookswap"]),
    ("Esplorazione e attività", "Meditazioni", {"cnt": "meditazioni"}, 15, ["meditazioni"]),
    ("Esplorazione e attività", "Fenicotteri di cocaina distrutti", {"cnt": "flamingos"}, 100, ["flamingos"]),
    ("Esplorazione e attività", "Playlist uniche", {"cnt": "playlists"}, 2, ["playlists"]),
    ("Esplorazione e attività", "Stili scoperti", {"cnt": "styles"}, 70, []),
    ("Esplorazione e attività", "Gare uniche vinte", {"cnt": "races"}, 30, ["races"]),
    ("Esplorazione e attività", "Ori nelle sfide di gara", {"cnt": "racech"}, 10, ["racech"]),
    ("Esplorazione e attività", "Ori ai poligoni", {"cnt": "shoot"}, 42, ["shoot"]),
    ("Esplorazione e attività", "Videogiochi giocati", {"cnt": "videogames"}, 4, ["videogames"]),
    ("Esplorazione e attività", "Avversari di biliardo battuti", {"cnt": "pool"}, 5, ["pool"]),
    ("Esplorazione e attività", "Minigolf giocati", {"cnt": "golf"}, 2, ["golf"]),
    ("Esplorazione e attività", "Canestri", {"cnt": "hoops"}, 90, ["hoops"]),
    ("Esplorazione e attività", "Time trial dei droni", {"cnt": "droneTT"}, 42, ["drone"]),
    ("Esplorazione e attività", "Acrobazie", {"cnt": "stunts"}, 300, ["stunt", "knife", "base"]),
    ("Esplorazione e attività", "Sfide completate", {"cnt": "challenges"}, 70, ["challenges"]),
    ("Esplorazione e attività", "Mazzi di caccia di Bret", {"cnt": "bret"}, 15, []),
    ("Scoperte", "Veicoli base scansionati", {"cnt": "vehicles"}, 200, []),
    ("Scoperte", "Armi standard trovate", {"cnt": "weapons"}, 50, []),
    ("Scoperte", "Animali studiati", {"cnt": "animals"}, 100, []),
]

GANGOPS = [
    ("Kingfishers", ["Fishing Shacks", "Sunrise RV Park", "Manatee Motel"]),
    ("Kolts & Associates", ["Kingpin Bowling", "June Warehouse", "La Cascara Motel", "Brooks Boatworks", "Stash House"]),
    ("M7", ["M7 Compound", "Weed Grow"]),
    ("La Polilla Negra", ["Palmer Fishing Warehouse", "Watson Bay Safehouse"]),
    ("Final Chapter", ["Farm Fix Meth Lab", "Biker Hideout", "Hog Stars Garage", "Irons Building Supply"]),
    ("San4San", ["Sound4Sond Studio", "La Perle Trap House", "Illegal Sneaker Trade", "JanJak's Garage", "Parlor Apartments"]),
    ("PTT Youngin$", ["Southside Trap House", "Kamar Devon Community Center"]),
    ("The Guardia Brothers", ["Saber Shipping Yard", "Casa Guardia", "Saber Shipping Facility"]),
    ("Altri criminali", ["Exotic Animals Front", "Mill Station Radar Base", "Industrial Weed Grow", "Slator Towing Inc", "Leonida Carrier Warehouse",
                         "Cigar Import Front", "Chatfield Storage & Logistics", "Ocean Beach Lab", "Vespucci Mansion", "Gas Station Meth Front",
                         "Walker Farm", "Backroom Weed Front", "Carter Mining Boathouse"]),
]
GANGOP_PINS = {"Sunrise RV Park": "L265"}

COLLECT_GUIDES = ["meditazioni", "carte", "waink", "stunt", "knife", "base", "shoot", "drone", "races", "racech", "challenges",
                  "magazines", "bookswap", "flamingos", "playlists", "videogames", "pool", "golf", "hoops", "effigies", "gangops",
                  "banks", "payday", "smash", "kitty", "fences"]


def build(slugify, at):
    import re
    def tid(n): return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")
    trophies = []
    for (n, g, h, d, tip, ch, link) in TROPHIES:
        t = {"id": tid(n), "n": n, "g": g, "h": h, "d": d, "tip": tip, "ch": ch,
             "links": [GUIDES[k] for k in TROPHY_LINKS.get(n, [])] + [GUIDES["trophyguide"]]}
        if link: t.update(link)
        trophies.append(t)
    hundred = [{"s": s, "n": n, "t": t, "links": [GUIDES[k] for k in gl], **k} for (s, n, k, t, gl) in HUNDRED]
    gang = []
    for g, ops in GANGOPS:
        items = []
        for o in ops:
            it = {"id": tid(g + "-" + o), "n": o}
            if o in GANGOP_PINS: it["p"] = at(GANGOP_PINS[o])
            items.append(it)
        gang.append({"g": g, "ops": items})
    return {"trophies": trophies, "hundred": hundred, "gangops": gang, "counters": COUNTERS,
            "guides": [GUIDES[k] for k in COLLECT_GUIDES]}
