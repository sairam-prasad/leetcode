class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        li =[]
        for i in range(len(nums)):

            if nums[i]==target:
                li.append(i)
                break
        if len(li)==0:
            li.append(-1)
        for i in range(len(nums)-1,-1,-1):

            if nums[i]==target:
                li.append(i)
                break
        
        if len(li)==1:
            li.append(-1)
        return li
        