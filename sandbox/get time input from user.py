import sys
time=raw_input("Enter time to shutdown pc after HH:mm:")
hh=time[0:2]
mm=time[3:5]
print hh
print mm
hour_to_sec=(60*60)
min_to_sec=60
hh=int(hh)
mm=int(mm)
sleep_time_sec=(hh*hour_to_sec)+(mm*min_to_sec)
print sleep_time_sec

x=raw_input("Time is")
