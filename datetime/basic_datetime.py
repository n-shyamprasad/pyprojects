'''
Print current date and time in Python
'''
import datetime as dt
from time import gmtime, strftime

print(f"datetime.now: {dt.datetime.now()}")
print(f"datetime.now().date: {dt.datetime.now().date()}")
print(f"datetime.now().time: {dt.datetime.now().time()}")
print(f"datetime.now().timestamp: {dt.datetime.now().timestamp()}")
print(f"datetime.now().timestamp: {dt.datetime.now().day}")


# strftime
print("datetime from strftime: ", strftime("%Y/%m/%d %H:%M:%S", gmtime()))