import time
def countdown(n):
    while n>0:
        print n
        n=n-1
        time.sleep(1)
        if n==0:
            print "blast off"

countdown(20)
    
