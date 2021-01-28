from itertools import combinations  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums) - 1):
             for y in range(x + 1, len(nums)):
                      if( (nums[x] + nums[y])== target):
                            return([x,y])
