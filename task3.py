import turtle
class point():
        """point"""
point1=point()
point1.x=1
point1.y=100
bob=turtle.Turtle()


"""def move_turtle(t, point):
    t.penup()
    t.setpos(point.x, point.y)
    t.pendown()"""

"""def draw_rect(t):
    move_turtle(t,point1)
    for i in range(0,4):
        t.fd(200)
        t.lt(90)
draw_rect(bob)"""

def polygon(bob,length,n):
	a=360/n
	for i in range(n):
		bob.fd(length)
		bob.lt(a)

def cir(t,r):
    circum=2*3.147*r
    polygon(t,circum/1000,1000)

cir(bob,100)

turtle.mainloop()