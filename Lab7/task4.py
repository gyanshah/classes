class IPv4:
	def __init__(self,x,m):
		self.x=x
		self.m=m
	def getNetwork(self):
		network=[]
		if self.x&m==1:
			network=[self.x]
		else:
			network.append(0)
		return network

ipv4=IPv4([10,0,1,7],24)
net=ipv4.getNetwork()
print(net)
