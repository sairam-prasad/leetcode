class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res =-1
        li =[]
        low,high = 0, len(nums)-1

        while low<=high:

            mid = (low+high)//2

            if nums[mid]==target:
                res = mid
                high =mid-1

            elif nums[mid]<target:
                low = mid+1
            
            elif nums[mid]>target:
                high = mid-1
            
            else:
                li.append(mid)
                break
        if len(li)==0:
            li.append(res)
        print(li)
        res =-1

        low,high = 0, len(nums)-1

        while low<=high:

            mid = (low+high)//2

            if nums[mid]==target:
                res =mid
                low = mid+1
            if nums[mid]>target:
                high = mid-1
            
            elif nums[mid]<target:
                low = mid+1
            
            
        if len(li)==1:
            li.append(res)
        print(li)

        return li