'''
Print a date in a the following format
Day_name  Day_number  Month_name  Year

Input: given_date = datetime(2020, 2, 25)
Output: Tuesday 25 February 2020
'''
from datetime import datetime as dtt
given_date = dtt(2020, 2, 25)
print(f"Given Date: {given_date}")
print(f"Formatted: {given_date.strftime('%A %d %B %Y')}")