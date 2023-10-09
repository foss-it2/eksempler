"""
Ta utgangspunkt i eksemplet med karakterer ovenfor. 
Gjør om utskriften slik at vi får "3, 4, 6, 6, 5 og 4" på slutten, 
altså «og» i stedet for komma før siste karakter.
"""

navn = "Pål"
karakterer = [3, 4, 6, 6, 5, 4]

karaktertekst = ""
for i in range(len(karakterer)):
    if i > 0 and i < len(karakterer)-1:
        karaktertekst += ", " 
    elif i == len(karakterer) - 1:
        karaktertekst += " og "
    karaktertekst += str(karakterer[i])
print(f"{navn} fikk karakterene {karaktertekst}")