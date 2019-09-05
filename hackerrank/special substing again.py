#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def allCharactersSame(s) : 
    n = len(s) 
    for i in range(1, n) : 
        if s[i] != s[0] : 
            return False
    return True

def substrCount(n, s):
    count=0
    count+=n
    sub_str=[]
    for Len in range(1,n + 1): #from 1 to len of str Len=1
                ####(1,2,3,4,5)
        # Pick ending point 
        for i in range(n - Len + 1): #n=len of str - Len = 1 + 1 #all other                 expect chr which is in consideration
                #####(5-1+1=5)=>(0,1,2,3,4)
            # Print characters from current 
            # starting point to current ending 
            # point. 
            j = i + Len - 1 ## 0 + 1 -1 => 0
            #print("Len %s i %s j %s "%(Len,i,j))
            temp=""
            for k in range(i,j + 1): ##(0,0+1=1-1=0)
                temp+=s[k] ##when j=0 it will print a
            sub_str.append(temp)
    
    #print(sub_str)
    temp_str=[]
    for el in sub_str:
        #print(el)
        l=len(el)
        if(l%2==0):
            res = allCharactersSame(el)
            if res:
                temp_str.append(el)
        if(l%2 != 0):
            if(l>1):
                i=l//2
                temp=el.replace(el[i],"")
                res =allCharactersSame(temp)
                if res:
                    temp_str.append(el)

        #print(sub_str)
    
    #print(temp_str)
    return count+len(temp_str)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#########################
#Right Solution
#########################

# def substrCount(n, s):
#     tot = 0
#     count_sequence = 0
#     prev = ''
#     for i,v in enumerate(s):
#         # first increase counter for all seperate characters
#         count_sequence += 1
#         if i and (prev != v):
#             # if this is not the first char in the string 
#             # and it is not same as previous char, 
#             # we should check for sequence x.x, xx.xx, xxx.xxx etc
#             # and we know it cant be longer on the right side than
#             # the sequence we already found on the left side.
#             j = 1
#             while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
#                 # make sure the chars to the right and left are equal
#                 # to the char in the previous found squence
#                 if s[i-j] == prev == s[i+j]:
#                     # if so increase total score and step one step further out
#                     tot += 1
#                     j += 1
#                 else:
#                     # no need to loop any further if this loop did 
#                     # not find an x.x  pattern
#                     break
#             #if the current char is different from previous, reset counter to 1
#             count_sequence = 1  
#         tot += count_sequence            
#         prev = v
#     return tot    