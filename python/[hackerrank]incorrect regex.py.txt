#regex
import re
t=int(input())
for i in range(t):
    s=input()
    try:
        print(bool(re.compile(s)))
    except re.error:
        print('False')
    
