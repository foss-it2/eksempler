"""
1)	Lag en funksjon som tar en tekststreng som input. Statistikk over tegnene i teksten skal printes ut.
2)	Lag en funksjon som tar en liste med tall som input. Gjennomsnittet og summen av tallene i listen skal printes ut.
3)	Lag en funksjon som tar en liste med tall som input. En sortert liste skal printes ut samt medianen av tallene.

"""

# 1)

def get_statistikk(tekst):
    statistikk = {}
    # Går gjennom tekst med for løkke
    for c in tekst:
        if c not in statistikk:
            statistikk[c] = 1
        else:
            statistikk[c] += 1
    return statistikk


tekst = "asdf"*500
minStatistikk = get_statistikk(tekst)
for key in minStatistikk:
    print(f"{key} har frekvens {minStatistikk[key]}")


# 2)
def get_gjennomsnitt_sum_median(liste):
    sum = 0
    for tall in liste:
        sum += tall
    gjennomsnitt = sum / len(liste)
    sortert = sorted(liste)
    if len(liste) % 2 == 0:
        midten = len(liste)//2 - 1  # Heltallsdivisjon får nærmeste tall over midten.
        median = (sortert[midten] + sortert[midten+1]) / 2
    else:
        midten = len(liste)//2
        median = sortert[midten]

    return sum,gjennomsnitt,median

minSum, mittGjennomsnitt, median = get_gjennomsnitt_sum_median([2,4,3,3,4,5,6,5,4,3,5,6,5,4,3,5,6,58,89,7,654,34,33])
print(f"sum: {minSum}")
print(f"gjenomsnitt: {mittGjennomsnitt:.1f}")
print(f"median: {median:.1f}")