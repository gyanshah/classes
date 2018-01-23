class time():
    """Time"""
t=time()
t.hour=0
t.minute=20
t.seconds=50

def print_time(time):
    print("The current time is " '%.2d:%.2d:%.2d'%(time.hour,time.minute,time.seconds))

print_time(t)
