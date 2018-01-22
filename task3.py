import math
import turtle
class point():
        """point"""
point1=point()
point1.x=1
point1.y=100
bob=turtle.Turtle()


def move_turtle(t, point):
    t.penup()
    t.setpos(point.x, point.y)
    t.pendown()

"""def draw_rect(t):
    move_turtle(t,point1)
    for i in range(0,4):
        t.fd(200)
        t.lt(90)
draw_rect(bob)"""

def cir(t):
	move_turtle(t,point1)
	for i in range(360):
		t.fd(1)
		t.lt(1)

cir(bob)

turtle.mainloop()