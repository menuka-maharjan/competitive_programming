class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            res=dividend//divisor
        else:
            res=-1*((-1*dividend)//divisor)
        if res>0:
            return min(res,2**31 -1)
        else:
             return max(res,-2**31)