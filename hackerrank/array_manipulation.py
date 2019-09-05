#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #print(n)
    #print(queries)
    op_list = [0]*n
    #print(op_list)

    for row in queries:
        start=row[0]-1
        end=row[1]-1
        operation =row[2]

        #print(str(start)+str(end)+str(operation))
        #print(op_list[start:end+1])
        #for x in range(len(op_list[start:end+1])):
        op_list[start]=op_list[start]+operation

        if row[1] != len(op_list):
            op_list[row[1]] -= row[2]
        start+=1
    maxval = 0
    itt = 0
    print(op_list)
    for q in op_list:
        
        itt += q
        print("value of itt"+str(itt))
        print("value of q"+str(q))
        if itt > maxval:
            maxval = itt
    return maxval

#solution 2

# def arrayManipulation(n, queries):
#     arr = [0]*n
#     for i in queries:
#         arr[i[0] - 1] += i[2]
#         if i[1] != len(arr):
#             arr[i[1]] -= i[2]
#     maxval = 0
#     itt = 0
#     print(arr)
#     #print(max(arr))

# dont use max()to calculate maximum from list
#ADDING the val of list and making it max
#     for q in arr:
        
#         itt += q
#         print("value of itt"+str(itt))
#         print("value of q"+str(q))
#         if itt > maxval:
#             maxval = itt
#     return maxval



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
