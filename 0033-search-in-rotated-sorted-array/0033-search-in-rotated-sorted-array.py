class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low,high = 0,len(nums)-1

        res=-1
        k=target
        while(low<=high):

            mid = (low+high)//2

            if nums[mid]==target:
                return mid
            
            #left half sorted
            if nums[low]<=nums[mid]:
                if nums[low]<= k and k<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
                
            else:
                if nums[high]>=k and k>=nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
        return -1