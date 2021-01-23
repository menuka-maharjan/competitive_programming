k=int(input())
l1=list(map(int,input().split()))
import collections
l2=[item for item, count in collections.Counter(l1).items() if count == 1]
for x in l2:
    print(x)
