#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # print(len(arr))
    sum_of_hr_glass = []
    itt = 0
    row = len(arr)
    col = len(arr[0])
    if row<3 or col<3 :
        return -1
    for m in range(0,row-2):
        for n in range(0,col-2):
            sum = arr[m][n]+arr[m][n+1]+arr[m][n+2]+arr[m+1][n+1]+arr[m+2][n]+arr[m+2][n+1]+arr[m+2][n+2]
            sum_of_hr_glass.append(sum)
    #print(sum_of_hr_glass)
    return max(sum_of_hr_glass)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
