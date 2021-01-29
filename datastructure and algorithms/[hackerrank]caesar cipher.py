#Caesar Ciphr
n=int(input())
s=input()
k=int(input())
l1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l2=[x.upper()for x in l1]
l=[a for a in s]
l3=[]
for y in l:
    if y.islower():
        j=(l1.index(y)+k)%26
        l3.append(l1[j])
    elif y.isupper():
        j=(l2.index(y)+k)%26
        l3.append(l2[j])
    else:
        l3.append(y)
s1=""
print(s1.join(l3))        
