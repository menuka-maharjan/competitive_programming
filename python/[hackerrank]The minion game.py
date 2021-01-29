def minion_game(string):
    
    # your code goes here
    string=string.upper()
    v=0
    c=0
    for i in range(len(string)):
        if(string[i]in"AEIOU"):
            v+=(len(string)-i)
        else:
            c+=(len(string)-i)
    if(v>c):
        print("Kevin",v)
    elif(v<c):
        print("Stuart",c)
    else:
        print("Draw")
    return
