'''
    Problem 2
    Write a program that takes today’s date and prints the date of the next week.
    Ex:
    Input: 	  Day: 25 Month: 1 Year: 2025
    Output: Day: 1   Month: 2 Year: 2025
'''

import datetime

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

today = datetime.date(year, month, day)
nextWeek = today + datetime.timedelta(days = 7)

print(f"Day: {nextWeek.day}, Month: {nextWeek.month}, Year: {nextWeek.year}")
