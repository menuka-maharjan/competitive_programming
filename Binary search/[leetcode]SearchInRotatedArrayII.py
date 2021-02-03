class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        l=0
        r=n-1
        while(l<=r):
            while l < r and nums[l] == nums[l+1]:
                l+=1
            
            while l < r and nums[r] == nums[r-1]:
                r-=1
                
            mid = l + (r-l)//2
            if(nums[mid]==target):
                 return True
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
        return False