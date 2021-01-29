l2=[]
l1=list(map(int,input().rstrip().split()))
word=input()
for i in range(len(word)):
    a=l1[ord(word[i])-97]
    l2.append(a)
print(max(l2)*len(word))
    
