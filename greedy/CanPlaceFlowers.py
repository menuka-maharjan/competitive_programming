class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        if len(flowerbed)==1 and flowerbed[0]==0:
            return 1
        else:
            if flowerbed[0]==0 and flowerbed[1]!=1:
                flowerbed[0]=1
                c+=1
            if flowerbed[-1]==0 and flowerbed[-2]!=1:
                flowerbed[-1]=1
                c+=1
            for i in range(1,len(flowerbed)-2):
                if flowerbed[i]==0 and flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    c+=1
            return (c>=n) 