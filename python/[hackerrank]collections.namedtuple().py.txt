#collections.namedtuple
from collections import namedtuple
n=int(input())
s=input().split()
tmark=0
for i in range(n):
    st=namedtuple("st",s)
    s1,s2,s3,s4=input().split()
    st=st(s1,s2,s3,s4)
    tmark+=int(st.MARKS)
print('{:.2f}'.format(tmark/n))
