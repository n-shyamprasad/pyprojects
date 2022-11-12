'''
Convert string into a datetime object
Input: date_string = "Feb 25 2020 4:20PM"
Ouput: 2020-02-25 16:20:00
'''

from datetime import datetime as dt
date_string = "Feb 25 2020  4:20PM"
datetime_obj = dt.strptime(date_string, "%b %d %Y %I:%M%p")
print(datetime_obj)