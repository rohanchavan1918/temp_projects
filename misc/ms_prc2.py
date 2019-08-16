"""
Author: thund3rstorm
Given a alphanumeric string,
calculate sum of the integers present in the string.

e.g.-	Input-  thund3r45to4rm
		Output- 52	

"""

s=str(input("Enter String\n"))
ls=[]
op=[]
for i in s:
	if i.isnumeric()==True:
		ls.append(i)
	if i.isalpha()==True:
		ls.append(",")
st="".join(ls)
ls2=st.split(",")
for k in ls2:
	if k.isnumeric()==True:
		op.append(k)
tot=0
for j in op:
	tot=tot+int(j)
print(tot)
