# DateTools.py
A few date functions written in Python.

#### IsLeapYear(y)
Takes a year and determines whether that year is a leap year or not.

#### DayOfTheWeek(k, m, D, C)
Utilizes Zeller's Rule for finding the day of the week, where:
- k = day of the month
- m = number of the month (March is 1... February is 12)
- D = decade of the year (last two digits)
- C = century of the year (first two digits)

#### DaysBetween(m1,d1,y1,m2,d2,y2)
Takes the month, day, and year of two dates and calculates the total number of days between them.
