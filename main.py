# beräkna lön inkl. alla tillägg. Importera timmar från google kalender. Importera ob-tillägg
# från nätet. Använd jobbskuld för att räkna ut skatten.

basic_salary = 28000
salary_extra_hour = 190
extra_hours = int(input("Amount of extra hours: "))
ob = 4500
gross_salary = grundlon + ob + lon_extratimme * extratimmar

print("Gross salary:", gross_salary)

# Skattetabeller

if 30001 <= bruttolon <= 30200:
    skatt = 5943
elif 30201 <= bruttolon <= 30400:
    skatt = 5994
elif 30401 <= bruttolon <= 30600:
    skatt = 6045
elif 30601 <= bruttolon <= 30800:
    skatt = 6096
elif 30801 <= bruttolon <= 31000:
    skatt = 6147
elif 31001 <= bruttolon <= 31200:
    skatt = 6198
elif 31201 <= bruttolon <= 31400:
    skatt = 6250
elif 31401 <= bruttolon <= 31600:
    skatt = 6301
elif 31601 <= bruttolon <= 31800:
    skatt = 6352
elif 31801 <= bruttolon <= 32000:
    skatt = 6403
elif 32200 >= bruttolon >= 32001:
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

print("Taxes:", skatt)

nettolon = bruttolon - skatt

print("Net salary:", nettolon)
