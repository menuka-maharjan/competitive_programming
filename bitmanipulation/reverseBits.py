class Solution:
    def reverseBits(self, n: int) -> int:
        l=list("{:032b}".format(n))
        l.reverse()
        return(int("".join(l),2))