# Python3 program to print all possible 
# substrings of a given string 


# Function to print all sub strings 
def subString(Str,n): 
	#str =aaa
	
	# Pick starting point 
	for Len in range(1,n + 1): #from 1 to len of str Len=1
				####(1,2,3,4,5)
		# Pick ending point 
		for i in range(n - Len + 1): #n=len of str - Len = 1 + 1 #all other expect chr which is in consideration
				#####(5-1+1=5)=>(0,1,2,3,4)
			# Print characters from current 
			# starting point to current ending 
			# point. 
			j = i + Len - 1 ## 0 + 1 -1 => 0
			print("Len %s i %s j %s "%(Len,i,j))
			for k in range(i,j + 1): ##(0,0+1=1-1=0)
				print(Str[k],end="") ##when j=0 it will print a
			print() 
			
# Driver program to test above function 
Str = "aaaa"
subString(Str,len(Str)) 

# This code is contributed by mohit kumar 


"""################
OUTPUT
"""################

"""
Len 1 i 0 j 0
a
Len 1 i 1 j 1
a
Len 1 i 2 j 2
a
Len 1 i 3 j 3
a
Len 2 i 0 j 1
aa
Len 2 i 1 j 2
aa
Len 2 i 2 j 3
aa
Len 3 i 0 j 2
aaa
Len 3 i 1 j 3
aaa
Len 4 i 0 j 3
aaaa

"""
