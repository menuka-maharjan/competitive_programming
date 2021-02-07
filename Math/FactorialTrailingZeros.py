import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        x=math.factorial(n)
        x=str(x)
        y=len(x) - len(x.rstrip('0'))
        return y