'''
Find the day of the week of a given date

Input: given_date = datetime(2020, 7, 26)
Output: Sunday
'''

from datetime import datetime as dtt
given_date = dtt(2020, 7, 26)
print(f"Given date: {given_date}")
print(f"Day of week: {given_date.today().weekday()}")
print(f"Week Day: {given_date.strftime('%A')}")