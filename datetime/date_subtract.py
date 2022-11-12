'''
Subtract a week (7 days)  from a given date in Python
Input: given_date = datetime(2020, 2, 25)
Output: 2020-02-18
'''
from datetime import datetime as dt, timedelta

given_date = dt(2022, 2, 25)
print(f"Given date: {given_date}")
days_to_subtract = 7
new_date = given_date - timedelta(days=days_to_subtract)
print(f"New Date: {new_date}")