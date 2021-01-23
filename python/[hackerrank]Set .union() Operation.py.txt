# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
n1 = int(input())
s1 = set(map(int, input().split()))
s2=s.union(s1)
print(len(s2))
