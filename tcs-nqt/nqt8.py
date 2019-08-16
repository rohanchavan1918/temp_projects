"""
Author: thund3rstorm

TCSNQT NINJA CODING
Write a program to print the final position of a person based on the following:
The person starts from origin and then,
he first turns right and travels 10 units of distance
his second turn is Upward for 20 units
his third turn is to the left for 30 units
fourth turn is Downward for 40 units
fifth turn is right (again) for 50 units....
and thus he travels, every time increasing the travel distance by 10 units.
The output position is in form of (x,y) coordinates
"""
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
