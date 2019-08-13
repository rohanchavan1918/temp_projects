'''
Given a string of numbers (ex. 9871293712387 )
if the string is in Ascending or Descending order of numbers,
print the biggest number and then smallest number first.
else print the first substring of half of the length of string
if tne string is even length print l // 2 substring ,
 else  odd them print l //2 +1 substring 

'''


def check_ascending(l):
	poop = sorted(l)
	if l == poop :
		return True
	else:
		return False

def check_descending(l):
	poop = sorted(l,reverse=True)
	if l == poop :
		return True
	else:
		return False		


def convert_into_list(str):
	l = list(map(int,str))
	return l

def not_even_not_odd(s):
	if len(s)%2 == 0 :	
		p = len(s)//2
		j  = ""
	
		for i in range(0,p):
			j = j + str(s[i]) 
		return j
	else:
		p = len(s)//2
		j = ""
		for i in range(0,p+1):
			j = j+str(s[i])
		return j

string = str(input("enter the string input \n"))
int_str = convert_into_list(string)
if check_ascending(int_str) == True :
	#print("ascending")
	res = str(int_str[-1])+str(int_str[0])
	print(res)
	

elif check_descending(int_str) == True :
	#print("descending")
	print(str(int_str[0])+str(int_str[-1]))
else:
	s = not_even_not_odd(int_str)
	print(s)
