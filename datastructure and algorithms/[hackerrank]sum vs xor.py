n=int(input())
print(2**(bin(n).count('0')-1)-bool(not n))
