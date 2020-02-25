# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 00:34:11 2020

@author: Nathan
"""


#### Using Zeller's Rule for finding the day of the week.
# k = day of the month
# m = number of the month (March is 1... February is 12)
# D = last two digits of the year
# C = century of the year (first two digits)

DAYS = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
MONTHS = ["March","April","May","June","July","August",
          "September","October","November","December","January","February"]
MONTHS_INDEX = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,
                "July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
MONTHS_AND_DAYS = {"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,
                   "July":31,"August":31,"September":30,"October":31,"November":30,"December":31}

def getKey(d, val):
    for key, value in d.items():
        if val == value:
            return key

def IsLeapYear(y):
    if y%4 == 0:
        return True
    return False

def DayOfTheWeek(k, m, D, C):
    ## Using double-slash for integer division
    f = k + ((13*m - 1)//5) + D + (D//4) + (C//4) - (2*C)
    r = f%7
    return DAYS[int(r)]

print(DayOfTheWeek(29,11,63,20))

def DaysBetween(m1,d1,y1,m2,d2,y2):
    totalDays = 0
    currentDay = d1
    currentMonth = m1
    monthCount = 0
    yearDiff = int(y2)-int(y1)
    currentYear = y1
    ####
    while True:
        if (currentDay == d2) and (currentMonth == m2) and (currentYear == y2):
            return totalDays
        if currentDay == MONTHS_AND_DAYS[currentMonth]:
            if IsLeapYear(currentYear) and (currentMonth == MONTHS[-1]):
                totalDays += 1
            currentDay = 0
#            if monthCount == 12:
##                currentYear += 1
#                #currentMonth = m1
#                monthCount = 0
#            monthCount += 1
            if currentMonth == "December":
                currentMonth = "January"
                currentYear += 1
            else:
                currentMonth = getKey(MONTHS_INDEX, MONTHS_INDEX[currentMonth]+1)
        currentDay += 1
        totalDays += 1
        print("It is {0} {1}, {2} total days have elapsed".format(currentMonth, currentDay, totalDays))
            


############ Just need to build out business days between.
#### Combines above two functions, skipping count on any days that are weekends.
            