"""
Minste ordbok i verden.
"""
ordbok = {
    "nøkkel": 42
}

# Hente ut verdi
verdi = ordbok["nøkkel"]
print(verdi)

# Printe ut alle verdier i ordboken
for key in ordbok:
    print(key, ":", ordbok[key])

ordbok["nøkkel"] = 3.14
print(ordbok["nøkkel"])

if "nøkkel" in ordbok:
    ordbok.pop("nøkkel")

print(ordbok)