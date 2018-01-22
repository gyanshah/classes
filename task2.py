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
"""def find_center(rect):
    p=point()
    p.x=(rect.corner.x+rect.width)/2
    p.y=(rect.corner.y+rect.length)/2
    return p"""

def move_rectangle(rect,dx,dy):
    rect.width+=dx
    rect.length+=dy
    return rect.width,rect.length
print("The new coordinates of the rectangle are:(%g,%g)"%move_rectangle(rect,50,100))