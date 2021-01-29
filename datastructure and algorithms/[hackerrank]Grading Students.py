
def grade(x,n):
    if(x>=38):
        while(x%5!=0):
            x=x+1
        if(x-y<3):
            return (x)
        else:
            return (y)
    else:
         return (x)
n=int(input())
for i in range(n):
    x=int(input())
    y=x
    z=grade(x,n)
    print(z)
        
    
