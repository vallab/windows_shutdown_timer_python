import sys
import time
import os

debug=True

def countdown(n):
    while n>0:
        print n
        time.sleep(60)
        n=n-1
def get_time_from_user():
    
    time1=raw_input("Enter time to shutdown pc after HH:mm:")
    hh=int(time1[0:2])
    mm=int(time1[3:5])
    sleep_time_min=(hh*60)+(mm)
    n=sleep_time_min
    return n

n=get_time_from_user()
countdown(n)

if debug:
    print("Its working good, system will shutdown")
else:
    os.system('shutdown -s')







