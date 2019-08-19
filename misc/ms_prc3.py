"""
Author: thund3rstorm
------------------------------------
Given an array of integers, return a new array in which every index carries
the value of the product of the remaining elements.

Example:	i)	Given array [1,3,2,4,5] it would return
					Output: [120,40,60,30,24]
				ii)	Given array [4,10,3] it would return
					Output: [30,12,40]
"""
n=int(input("Enter number of elements\n"))
el=[]
for i in range(0,n):
	el.append(int(input("")))
print("Input List: ",el)

def prodf (x):
	prod=1
	for i in range(0,n):
		if i==x:
			pass
		else:
			prod=prod*el[i]
	return prod
opls=[]
for i in range(0,n):
	y=prodf(i)
	opls.append(y)		
print("Output List: ",opls)
