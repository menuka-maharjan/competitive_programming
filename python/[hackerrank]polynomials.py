import numpy
a=list(map(float,input().rstrip().split()))
x=int(input())
print (numpy.polyval(a, x))
