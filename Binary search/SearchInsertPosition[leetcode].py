class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x in nums:
            if x==target:
                return nums.index(x)
        nums.append(target)
        nums.sort()
        return nums.index(target)