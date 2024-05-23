import json

# Funksjon for å lese data fra JSON-filen
def les_datafil(filnavn):
    with open(filnavn, 'r') as fil:
        data = json.load(fil)
    return data

# Funksjon for å telle antall verdier i datasettet
def tell_verdier(data):
    return len(data['value'])

# Funksjon for å finne antall år med data
def antall_aar(data):
    return len(data['dimension']['Tid']['category']['index'])

# Funksjon for å finne gjennomsnittlig tid brukt på forskjellige medier
def gjennomsnitt_tid_per_medie(data):
    medie_index = data['dimension']['Media']['category']['index']
    tid_index = data['dimension']['Tid']['category']['index']
    

    resultater = {}
    for medie, idx in medie_index.items():
        totale_minutter = 0
        antall_verdier = 0
        for tid, tid_idx in tid_index.items():
            verdi_idx = idx * len(tid_index) + tid_idx
            verdi = data['value'][verdi_idx]
            if verdi is not None:
                totale_minutter += verdi
                antall_verdier += 1
        if antall_verdier > 0:
            gjennomsnitt = totale_minutter / antall_verdier
        else:
            gjennomsnitt = None
        medie_navn = data['dimension']['Media']['category']['label'][medie]
        resultater[medie_navn] = gjennomsnitt
    return resultater

# Funksjon for å finne årlig bruk av et bestemt medie
def aarlig_bruk_av_medie(data, medie_navn):
    medie_index = data['dimension']['Media']['category']['index']
    tid_index = data['dimension']['Tid']['category']['index']

    medie_kode = None
    for kode, navn in data['dimension']['Media']['category']['label'].items():
        if navn == medie_navn:
            medie_kode = kode
            break

    if medie_kode is None:
        return None

    resultater = {}
    for tid, tid_idx in tid_index.items():
        verdi_idx = medie_index[medie_kode] * len(tid_index) + tid_idx
        verdi = data['value'][verdi_idx]
        if verdi is not None:
            resultater[data['dimension']['Tid']
                       ['category']['label'][tid]] = verdi
    return resultater


def testeStruktur(data):
    print(type(data))   # Viser at det er en dict
    # Printer ut alle nøklene for en oversikt
    for key in data:
        print(key)
    oppdeling = data["label"]
    x_aksens_oppdelinger = data["size"]
    print(oppdeling)
    tidsindekser = data["dimension"]["Tid"]["category"]["index"]
    tid = data["dimension"]["Tid"]["category"]["label"]
    overskrifter = data["dimension"]["Media"]["category"]["label"]
    verdier = data["value"]
    print(overskrifter)
    medie_index = data['dimension']['Media']['category']['index']
    tid_index = data['dimension']['Tid']['category']['index']
    print(medie_index)
    print(tid_index)
    # Ønsker å finne årlig bruk av medier etter medietype

    


# Hovedprogram


def hovedprogram():
    filnavn = 'mediebruk_jsonified.json'  # Filnavn på JSON-datasettet
    data = les_datafil(filnavn)

    testeStruktur(data)

    #exit()

    print(f"Antall verdier i datasettet: {tell_verdier(data)}")
    print(f"Antall år med data: {antall_aar(data)}")

    gjennomsnitt_tid = gjennomsnitt_tid_per_medie(data)
    print("\nGjennomsnittlig tid brukt på forskjellige medier (minutter):")
    for medie, tid in gjennomsnitt_tid.items():
        print(
            f"{medie}: {tid:.2f} minutter" if tid is not None else f"{medie}: Ingen data")

    medie_navn = "TV"
    aarlig_bruk = aarlig_bruk_av_medie(data, medie_navn)
    print(f"\nÅrlig bruk av mediet '{medie_navn}' (minutter):")
    for aar, tid in aarlig_bruk.items():
        print(f"{aar}: {tid} minutter")


if __name__ == "__main__":
    hovedprogram()
