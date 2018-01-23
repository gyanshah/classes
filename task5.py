from datetime import datetime
class time():
    """Time"""
t=time()
def print_time(time):
    print("The current time is ",datetime.now().strftime('%H:%M:%S'))

print_time(t)
