'''
Calculate number of days between two given dates
I/P:
# 2020-02-25
date_1 = datetime(2020, 2, 25)

# 2020-09-17
date_2 = datetime(2020, 9, 17)

O/p:
205 days
'''

from datetime import datetime

def date_diff(date1, date2):
    delta = None
    if date1 > date2:
        print("date1 is greater")
        delta = date1 - date2
    else:
        print("date2 is greater")
        delta = date2 - date1
    print(f"Difference is {delta.days} days")


date1 = datetime(2020, 2, 25).date()
date2 = datetime(2020, 9, 17).date()
date_diff(date1, date2)
