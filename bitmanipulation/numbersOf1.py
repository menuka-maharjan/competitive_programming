class Solution:
    def hammingWeight(self, n: int) -> int:
        f=1
        c=0
        while(n):
            if(n&f==0):
                pass
            else:
                c+=1
            n>>=1
        return c