"""
1.	Lag inputfelt som tar inn en lang tekst (kopier fra nyhetssider, leksikon e.l.)
2.	Gjør om teksten til en liste.
3.	Gå gjennom listen og tell antall forekomster av hvert tegn. 
Antall forekomster legges inn i en ordbok der key er bokstav og verdi er antall forekomster. 
(For å slippe å skrive inn hver eneste bokstav i ordboken kan man for hver bokstav man 
undersøker sjekke om den allerede ligger i ordboken eller ikke.)
4.	Hvilke bokstaver skiller seg ut?
"""

langtekst = "ertyuiopl,mnbgfdcvbhjkihytgrertyhj"

tekst = list(langtekst)

statistikk = {}

for bokstav in tekst:
    if bokstav in statistikk:
        statistikk[bokstav] += 1
    else:
        statistikk[bokstav] = 1

print(statistikk)

# Sorterer ordboken etter synkende frekvens.
# ChatGPT 18. okt 2023 hjalp til med dette kompliserte lambdauttrykket vi ikke trenger å 
# forstå, bare bruke.
sorted_dict = dict(sorted(statistikk.items(), key=lambda item: item[1], reverse=True))

# Legg den sorterte ordboken inn i en liste
# ChatGPT hjalp til nok en gang! (Måtte rette opp å legge til .items() for det ble glemt.)
sorted_list = [(key, value) for key, value in sorted_dict.items()]
for pair in sorted_list:
    print(pair)