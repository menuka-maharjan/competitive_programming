class Solution:
    def convertToTitle(self, n: int) -> str:
        l=[chr(x) for x in range(ord('A'),ord('Z')+1)]
        l1=[]
        while n>0:
            x=l[(n-1)%26]
            l1.append(x)
            n=(n-1)//26
        l1.reverse()
        return ("".join(l1))