class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
       array = {}

       for i in range(len(nums)):
        if array.get(nums[i]):
            array[nums[i]]= array.get(nums[i])+1
        else:
            array[nums[i]]=1

        for key, value in array.items():

            if value > len(nums)//2:
                return key
                