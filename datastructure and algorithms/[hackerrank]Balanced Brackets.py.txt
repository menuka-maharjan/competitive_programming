n=int(input())
brackets={')':'(', '}':'{',']':'['}
for _ in range(n):
    string=input()
    stack=list()
    for char in string:
        if stack and stack[-1] == brackets.get(char):
            stack.pop()
        else:
            stack.append(char)
    if(len(stack)==0):
        print("YES")
    else:
        print("NO")
