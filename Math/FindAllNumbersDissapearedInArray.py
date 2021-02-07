class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s={x for x in range(1,n+1)}
        nums=list(s-set(nums))
        return nums