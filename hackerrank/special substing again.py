#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    tot = 0
    count_sequence = 0
    prev = ''
    for i,v in enumerate(s):
        # first increase counter for all seperate characters
        count_sequence += 1
        if i and (prev != v):
            # if this is not the first char in the string 
            # and it is not same as previous char, 
            # we should check for sequence x.x, xx.xx, xxx.xxx etc
            # and we know it cant be longer on the right side than
            # the sequence we already found on the left side.
            j = 1
            while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
                # make sure the chars to the right and left are equal
                # to the char in the previous found squence
                if s[i-j] == prev == s[i+j]:
                    # if so increase total score and step one step further out
                    tot += 1
                    j += 1
                else:
                    # no need to loop any further if this loop did 
                    # not find an x.x  pattern
                    break
            #if the current char is different from previous, reset counter to 1
            count_sequence = 1  
        tot += count_sequence            
        prev = v
    return tot    
    return count+len(temp_str)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


