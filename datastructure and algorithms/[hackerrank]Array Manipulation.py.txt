#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    l= [0] * (n+1)
    for _ in range(m):
        a,b,k=(map(int, input().rstrip().split()))
        l[a-1] += k
        if b <= len(l):
            l[b]-=k
    max=sum=0        
    for i in l:
        sum+=i
        if sum > max:
            max=sum
    fptr.write(str(max) + '\n')
    fptr.close()
