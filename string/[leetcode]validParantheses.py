class Solution:
    def isValid(self, s: str) -> bool:
        brackets={')':'(', '}':'{',']':'['}
        stack=list()
        for char in s:
            if stack and stack[-1] == brackets.get(char):
                stack.pop()
            else:
                stack.append(char)
        if(len(stack)==0):
            return True
        else:
            return False