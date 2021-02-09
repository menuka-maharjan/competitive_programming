class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=[]
        for i in range(len(prices)-1):
            if(prices[i+1]>prices[i]):
                l.append(prices[i+1]-prices[i])
        return sum(l)