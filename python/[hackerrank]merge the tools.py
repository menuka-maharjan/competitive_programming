def merge_the_tools(string, k):
    from collections import OrderedDict
    n=len(string)
    d=int(n/k)
    l=[]
    i=0
    ol=OrderedDict()
    while(i!=n):
        a=str(string[i:i+k])
        i+=k
        l.append("".join(OrderedDict.fromkeys(a))) 
    for j in range(0,len(l)): 
        print(l[j])
