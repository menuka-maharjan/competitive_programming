class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s={x for x in range(0,n+1)}
        nums=list(s-set(nums))
        return nums[0]