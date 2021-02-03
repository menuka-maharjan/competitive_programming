class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        if target  not in nums:
            return ([-1,-1])
        else:
            l=[i for i,x in enumerate(nums) if x==target]
            return ([min(l),max(l)])