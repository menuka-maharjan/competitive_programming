class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        d=n-m+1
        res=0
        for i in range(0,32):
            if(d>(1<<i)):
                pass
            else:
                if((m & (1<<i)) & (n & (1<<i))):
                    res+=1<<i

        return res