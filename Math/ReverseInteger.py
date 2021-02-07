class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        y=str(abs(x))
        z=int(y[::-1])
        if x<0:
            z=-z
        if z<-2**31 or z>2**31-1:
            return 0
        if z<0:
            return max(z,-2**31)
        else:
            return min(z,2**31-1)
        
    
