import math
class point(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __add__(self,p):
		p.x=self.x+p.x
		p.y=self.y+p.y
		return p

p1=point(3,4)
p2=point(5,6)
print(p1.x+p2.x,p1.y+p2.y)
def distance_between_points(p1,p2):
    dx=p2.x-p1.x
    dy=p2.y-p1.y
    distance=math.sqrt((dx**2)+(dy**2))
    return distance

print("The distance between two points is:%f"%distance_between_points(p1,p2))
