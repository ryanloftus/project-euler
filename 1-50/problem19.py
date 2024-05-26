def days_in_month(month, year):
    if month in [9, 4, 6, 11]:
        return 30
    elif month == 2:
        return 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
    else:
        return 31

count = 0
month = 1
year = 1900

sundays = 0

while year < 2001:
    if year >= 1901 and count % 7 == 6:
        sundays += 1
    count += days_in_month(month, year)
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1

print(sundays)
