class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        l=0
        r=n-1
        while(l<=r):
            mid=(l+r)/2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>=nums[l]):
                if(target<=nums[mid] and target>=nums[l]):
                    r=mid-1
                else:
                    l=mid+1
            else:
                if(target>=nums[mid] and target<=nums[r]):
                    l=mid+1
                else:
                    r=mid-1
        return  -1