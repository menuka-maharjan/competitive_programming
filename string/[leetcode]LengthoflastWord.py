class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=[i for i in s.split()]
        if len(l)==0:
            return 0
        else:
            return(len(l[-1]))
        
        