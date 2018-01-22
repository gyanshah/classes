class time():
    """Time"""
t=time()
t.hour=16
t.minute=20
t.seconds=50

def print_time(time):
    print("The current time is ('%g':,'%g':,'%g'",% (time.hour,time.minute,time.seconds))

print_time(t)