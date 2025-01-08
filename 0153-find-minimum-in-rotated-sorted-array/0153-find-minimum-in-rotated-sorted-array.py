class Solution:
    def findMin(self, nums: List[int]) -> int:

        low,high = 0,len(nums)-1
        ans = 5000

        while low<=high:

            mid = (low+high)//2

            if nums[low]<=nums[high]:
                ans = min(ans,nums[low])
                break
            
            if nums[low]<=nums[mid]:
                ans = min(ans, nums[low])
                low = mid+1
            
            elif nums[mid]<=nums[high]:
                ans= min(ans, nums[mid])
                high = mid-1
        return ans

        