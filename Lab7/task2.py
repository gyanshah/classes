class point(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __add__(self,p):
		if isinstance(p,point):
			self.x+=p.x
			self.y+=p.y
			return self
		elif isinstance(p,tuple):
			self.x+=p[0]
			self.y+=p[1]
			return self

p1=point(3,4)
p2=point(10,11)
p3=p1+p2
print(p3.x,p3.y)
