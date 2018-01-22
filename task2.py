import math
class point():
    """class defination"""
class rectangle():
    """Width,height and corner are attributes"""
rect=rectangle()
rect.width=100
rect.length=200
rect.corner=point()
rect.corner.x=0
rect.corner.y=0
def find_center(rect):
    p=point()
    p.x=(rect.corner.x+rect.width)/2
    p.y=(rect.corner.y+rect.length)/2
    return p
center=find_center(rect)
print('The center of the rectangle is (%g,%g)'% (center.x,center.y))