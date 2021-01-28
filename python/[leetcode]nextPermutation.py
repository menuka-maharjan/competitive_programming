class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        if(n<=2):
            return nums.reverse()
        ptr=n-2
        while(ptr>=0 and nums[ptr]>=nums[ptr+1]):
            ptr-=1
        if(ptr==-1):
            return nums.reverse()
        for x in range(n-1,ptr,-1):
            if nums[ptr]<nums[x]:
                nums[ptr],nums[x]=nums[x],nums[ptr]
                break
        nums[ptr+1:]=reversed(nums[ptr+1:])
        return nums
            
        
        
        