#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    product=1
    count=0
    for num in range(0,n+1):
        flag=True
        if(num>1):
            for j in range(2,num):
                if flag and num%j==0:
                    flag=False
                    continue

            if flag :
                if product*num<=n: 
                    product*=num
                    count+=1
                else:
                    break
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
