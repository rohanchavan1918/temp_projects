#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    len_a = len(a) #20
    len_b = len(b) #30
    count=0

    if(len_a<1 and len_b<1):
        return -1
    a=a.lower()
    b=b.lower()

    # #this logic for duolicate element is not correct
    # l1 = len(set(a)) #11
    # l2 = len(set(b)) #21
    # print(l1)
    # print(l2)
    # temp1=""
    # temp2=""
    # a=temp1.join(list(set(a)))
    # b=temp2.join(list(set(b)))

    # # print(a)
    # # print(b)
    # #print(count)

    # #upto here

    for ch in a:
        if(ch not in b):
            #elements not present in b will come in
            # a.remove(ch) this doesnt work
            a = a.replace(ch,"")
            #or a.translate({ord('ch'): None})
            count+=1
            # print(ch)
            # print(a)
    for ch in b:
        if(ch not in a):
            #elements not present in a will come in
            # b.remove(ch) this doesnt work
            b = b.replace(ch,"")
            #or b.translate({ord('ch'): None}) will work
            count+=1
            # print(ch)
            # print(b)
    #for elements which are repeating
    #from a rxwsmligxvm
    #fron b xwrvlmriswmgm

    # {'v', 'w', 'l', 'g', 'r', 's', 'i', 'm', 'x'}
    # {'v', 'w', 'l', 'g', 'r', 's', 'i', 'm', 'x'} 

    return count

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()


#right solution

def makeAnagram(a, b):
    cnt = [0] * 26
    offset = ord('a')
    for char in a:
        cnt[ord(char) - offset] += 1
    for char in b:
        cnt[ord(char) - offset] -= 1
    total = 0
    for value in cnt:
        total += abs(value)
    return total