class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                if i!=j and nums[i]==nums[j]:
                    count=count+1
        return count
        