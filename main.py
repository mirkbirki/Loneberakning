# The program should calculate net salary, based on worked hours registered on google calendar. Might need a
# connection to "https://assistanskoll.se/ob.html?d=2020-01-01" for fetching salary supplements, for hours worked
# during inconvenient hours. Could possibly need a connection to "https://www.skatteverket.se/download/18.1997e70d18
# 48dabbac93531/Allm%C3%A4nna%20tabeller%20-%20m%C3%A5nad.pdf" for fetching taxes.

# Salary before any additional salary supplements.
basic_salary = 28000
# Salary for any extra hour worked.
salary_extra_hour = 190
# Amount of extra hours worked during the month.
extra_hours = int(input("Amount of extra hours: "))
# Salary supplements for hours worked during nights, weekends and holidays (inconvenient working hours).
salary_supplements = 4500
# Salary before taxes
gross_salary = basic_salary + salary_extra_hour * extra_hours + salary_supplements

print("Gross salary:", gross_salary)

# Tax table (can the table on "skatteverket" be used instead of all of the if/elif/else statements?)

if 30001 <= gross_salary <= 30200:
    taxes = 5943
elif 30201 <= gross_salary <= 30400:
    taxes = 5994
elif 30401 <= gross_salary <= 30600:
    taxes = 6045
elif 30601 <= gross_salary <= 30800:
    taxes = 6096
elif 30801 <= gross_salary <= 31000:
    taxes = 6147
elif 31001 <= gross_salary <= 31200:
    taxes = 6198
elif 31201 <= gross_salary <= 31400:
    taxes = 6250
elif 31401 <= gross_salary <= 31600:
    taxes = 6301
elif 31601 <= gross_salary <= 31800:
    taxes = 6352
elif 31801 <= gross_salary <= 32000:
    taxes = 6403
elif 32200 >= gross_salary >= 32001:
    taxes = 6454
elif 32400 >= gross_salary >= 32201:
    taxes = 6505
elif 32600 >= gross_salary >= 32401:
    taxes = 6556
elif 32800 >= gross_salary >= 32601:
    taxes = 6607
elif 33000 >= gross_salary >= 32801:
    taxes = 6658
elif 33400 >= gross_salary >= 33201:
    taxes = 6761
elif 33600 >= gross_salary >= 33401:
    taxes = 6812
elif 33800 >= gross_salary >= 33601:
    taxes = 6863
elif 34000 >= gross_salary >= 33801:
    taxes = 6914
elif 34200 >= gross_salary >= 34001:
    taxes = 6965
elif 34400 >= gross_salary >= 34201:
    taxes = 7016
elif 34600 >= gross_salary >= 34401:
    taxes = 7067
elif 34800 >= gross_salary >= 34601:
    taxes = 7118
elif 35000 >= gross_salary >= 34601:
    taxes = 7169
else:
    taxes = gross_salary * 0.3

print("Taxes:", taxes)

net_salary = gross_salary - taxes

print("Net salary:", net_salary)
