class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        stones.reverse()
        n=len(stones)
        while(n>=2):
            if stones[0]==stones[1]:
                del stones[0:2]
                n-=2
            elif stones[0]>stones[1]:
                x=stones[0]-stones[1]
                del stones[0:2]
                stones.append(x)
                n-=1
            stones.sort()
            stones.reverse()
        if len(stones)==0:
            return 0
        else:
            return stones[0]