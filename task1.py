import math
class point(object):
    """class defination"""
p1=point()
p2=point()
p1.x,p1.y=4,3
p2.x,p2.y=5,6

def distance_between_points(p1,p2):
    dx=p2.x-p1.x
    dy=p2.y-p1.y
    distance=math.sqrt(dx**2+dy**2)
    return distance

print("The distance between two points is:%f"%distance_between_points(p1,p2))