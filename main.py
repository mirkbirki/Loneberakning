# beräkna lön inkl. alla tillägg. Importera timmar från google kalender. Importera ob-tillägg
# från nätet. Använd jobbskuld för att räkna ut skatten.

grundlon = 28000
lon_extratimme = 190
extratimmar = int(input("Antal extratimmar: "))
ob = 4500
bruttolon = grundlon + ob + lon_extratimme * extratimmar

print("Bruttolon:", bruttolon)

#Skattetabeller

if bruttolon <= 32200 and bruttolon >= 32001:
    skatt = 6454
elif bruttolon <= 32400 and bruttolon >= 32201:
    skatt = 6505
elif bruttolon <= 32600 and bruttolon >= 32401:
    skatt = 6556
elif bruttolon <= 32800 and bruttolon >= 32601:
    skatt = 6607
elif bruttolon <= 33000 and bruttolon >= 32801:
    skatt = 6658
elif bruttolon <= 33400 and bruttolon >= 33201:
    skatt = 6761
elif bruttolon <= 33600 and bruttolon >= 33401:
    skatt = 6812
elif bruttolon <= 33800 and bruttolon >= 33601:
    skatt = 6863
elif bruttolon <= 34000 and bruttolon >= 33801:
    skatt = 6914
elif bruttolon <= 34200 and bruttolon >= 34001:
    skatt = 6965
elif bruttolon <= 34400 and bruttolon >= 34201:
    skatt = 7016
elif bruttolon <= 34600 and bruttolon >= 34401:
    skatt = 7067
elif bruttolon <= 34800 and bruttolon >= 34601:
    skatt = 7118
elif bruttolon <= 35000 and bruttolon >= 34601:
    skatt = 7169
else:
    skatt = bruttolon * 0.3

print("Skatt:", skatt)

nettolon = bruttolon - skatt

print("Nettolon:", nettolon)