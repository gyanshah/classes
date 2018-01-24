class Time():
	"time"
time=Time()
time.hour=11
time.minute=59
time.second=30

def time_to_int(time):
	minutes=time.hour*60+time.minute
	seconds=minutes*60+time.second
	return seconds

def int_to_time(seconds):
	time=Time()
	minutes,time.second=divmod(seconds,60)
	time.hour,time.minute=divmod(minutes,60)
	return time

def increment(time,addtime):
	seconds=time_to_int(time)
	return int_to_time(seconds+addtime)

def print_time(x):
	print("The time is %.2d:%.2d:%.2d"%(x.hour,x.minute,x.second))

print_time (time)
newtime=increment(time,70)
print_time(newtime)
