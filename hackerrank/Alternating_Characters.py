#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    min_del = 0
    temp=s
    curr=""
    nxt =""
    l =len(s)
    for x in s:
        if x!="A" and x!="B":
            return -1
    if(l==1):
        return 0 #not required
    if(s.count("A")==len(s)):
        return l-1 #not required
    if(s.count("B")==len(s)):
        return l-1 #not required

    #below logic handel all above condition
    if s[0] == "A":
        curr="A"
        nxt="B"
        for i in range(1,len(s)):
            if s[i]==nxt:
                temp1 = curr
                curr = nxt
                nxt  = temp1
            else:
                # temp=temp.replace(temp[i]," ")
                min_del+=1
    # elif s[0] == "B":
    else:
        curr="B"
        nxt="A"
        for i in range(1,len(s)):
            if s[i]==nxt:
                temp1 = curr
                curr = nxt
                nxt  = temp1
            else:
                # temp=temp.replace(temp[i]," ")
                min_del+=1
        
    # print(min_del)
    return min_del

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()


#today i wrote this code successfully with my own logic