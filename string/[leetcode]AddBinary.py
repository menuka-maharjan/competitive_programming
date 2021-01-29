class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=bin(int(a,2)+int(b,2))
        return(x[2:])