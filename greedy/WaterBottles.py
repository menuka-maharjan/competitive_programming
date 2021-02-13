class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles<numExchange:
            return numBottles
        elif numBottles==numExchange:
            return (numBottles+1)
        else:
            x=numBottles//numExchange
            y=numBottles%numExchange
            z=numBottles+x
            i=x+y
            while (i>=numExchange):
                x=i//numExchange
                y=i%numExchange
                z+=x
                i=x+y
            return (z)
