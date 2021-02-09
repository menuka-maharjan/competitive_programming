class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=0
        t=0
        if bills[0]!=5:
            return False
        else:
            for i in range(len(bills)):
                if bills[i]==5:
                    f+=1
                elif bills[i]==10:
                    t+=1
                    f-=1
                elif bills[i]==20:
                    if t>0:
                        t-=1
                        f-=1
                    else:
                        f-=3
                if f<0:
                    return False
            return True