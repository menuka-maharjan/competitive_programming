class Solution:
    def totalMoney(self, n: int) -> int:
        l=[1,2,3,4,5,6,7]
        s=sum(l)
        total=0
        if n<=7:
            return int((n*(n+1))/2)
        else:
            x=n//7
            for i in range(1,x+1):
                total+=s+7*(i-1)
            y=n%7
            for i in range(y):
                total += (x+i+1)
            return total

