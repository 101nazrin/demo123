def zeller(day, month, year):

    zday = day
    zmonth = month - 2
    zyear = year
    if zmonth < 1:   # special treatment of Jan and Feb
        zmonth = zmonth + 12
        zyear = zyear - 1

    zcent = zyear // 100
    zyear = zyear - 100 * zcent

    # calculating the weekday number
    w = (13 * zmonth - 1) // 5
    x = zyear // 4
    y = zcent // 4
    z = w + x + y + zday + zyear - 2 * zcent
    r = z % 7        # remainder of integer division

    # deal with negative values
    if r < 0:
        r = r + 7

    # Conversion of day number into name of the day.
    # Using dictionaries
    weekdays = {0: "Sunday", 1: "Monday", 2: "Tuesday",
                3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

    wkday = weekdays[r]

    return wkday


# reads the datestring
date = input("Please enter the data in the DD/MM/YYYY format: ")

# splits into 3 strings
sday, smonth, syear = date.split("/")

# converts into int
day = int(sday)
month = int(smonth)
year = int(syear)


print(zeller(day, month, year))
print(zeller(day, month, year))
