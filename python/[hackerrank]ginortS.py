s=input()
l=[i for i in s ]
l1=[]
l2=[]
l3=[]
l4=[]
for x in l:
    if x.islower():
        l1.append(x)
        
    elif x.isupper():
        l2.append(x)
        
    else:
        if(int(x)%2!=0):
            l3.append(x)
            
        else:
            l4.append(x)
l1.sort()
l2.sort()
l3.sort()
l4.sort()   
l5=l1+l2+l3+l4
str=""
print(str.join(l5))
