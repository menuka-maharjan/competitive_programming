if __name__ == '__main__':
    n = int(input())
    l=[]
    for _ in range(n):
        abc=input().split()
        a=abc[0]
        if(a=='insert'):
            b=int(abc[1])
            c=int(abc[2])
            l.insert(b,c)
        elif(a=='print'):
            print(l)
        elif(a=='remove'):
            b=int(abc[1])
            l.remove(b)
        elif(a=='append'):
            b=int(abc[1])
            l.append(b)
        elif(a=='sort'):
            l.sort()
        elif(a=='pop'):
            l.pop()
        elif(a=='reverse'):
            l.reverse()
        else:
            pass
