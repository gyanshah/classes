class time():
    """Time"""
t1=time()
t2=time()
t1.hour=21
t1.minute=20
t1.seconds=50
t2.hour=20
t2.minute=20
t2.seconds=50

def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.seconds) > (t2.hour, t2.minute, t2.seconds)


print(is_after(t1,t2))
