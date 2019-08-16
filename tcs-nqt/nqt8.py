def newRange(start,end,step):
	i = start
	while i < end:
		yield i
		i += step
	yield end
	
turns=int(input("Enter number of turns\n"))
x=0
y=0
c=10
for i in range(1,turns+1):
	if i in newRange(1,turns+1,4):
		x=x+c
	elif i in newRange(2,turns+1,4): #for Upward
		y=y+c
	elif i in newRange(3,turns+1,4): #for Left
		x=x-c
	elif i in newRange(4,turns+1,4): #for Downward
		y=y-c
	c=c+10
print("Final position of the person is %d %d" %(x,y))
