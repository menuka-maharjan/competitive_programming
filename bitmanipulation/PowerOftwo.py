class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(n):
            if(n&(n-1)==0):
                return True
            else:
                return False