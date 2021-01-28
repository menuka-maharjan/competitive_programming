class Solution(object):
    def threeSumClosest(self, nums, target):
        n=len(nums)
        min_dif=abs(nums[0]+nums[1]+nums[2]-target)
        value=nums[0]+nums[1]+nums[2]
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    diff1=abs(nums[i]+nums[j]+nums[k]-target)
                    if(diff1<min_dif):
                        min_dif=diff1
                        value=nums[i]+nums[j]+nums[k]
        return value
                    