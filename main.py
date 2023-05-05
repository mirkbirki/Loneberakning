# beräkna lön inkl. alla tillägg. Importera timmar från google kalender. Importera ob-tillägg
# från nätet. Använd jobbskuld för att räkna ut skatten.

grundlon = 28000
lon_extratimme = 190
extratimmar = int(input("Antal extratimmar: "))
ob = 4500
bruttolon = grundlon + ob + lon_extratimme * extratimmar

print("Bruttolon:", bruttolon)

# Skattetabeller

if 32200 >= bruttolon >= 32001:
    skatt = 6454
elif 32400 >= bruttolon >= 32201:
    skatt = 6505
elif 32600 >= bruttolon >= 32401:
    skatt = 6556
elif 32800 >= bruttolon >= 32601:
    skatt = 6607
elif 33000 >= bruttolon >= 32801:
    skatt = 6658
elif 33400 >= bruttolon >= 33201:
    skatt = 6761
elif 33600 >= bruttolon >= 33401:
    skatt = 6812
elif 33800 >= bruttolon >= 33601:
    skatt = 6863
elif 34000 >= bruttolon >= 33801:
    skatt = 6914
elif 34200 >= bruttolon >= 34001:
    skatt = 6965
elif 34400 >= bruttolon >= 34201:
    skatt = 7016
elif 34600 >= bruttolon >= 34401:
    skatt = 7067
elif 34800 >= bruttolon >= 34601:
    skatt = 7118
elif 35000 >= bruttolon >= 34601:
    skatt = 7169
else:
    skatt = bruttolon * 0.3

print("Skatt:", skatt)

nettolon = bruttolon - skatt

print("Nettolon:", nettolon)
