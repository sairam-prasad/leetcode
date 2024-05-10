class Solution:
    
    def setIntegers(self,n):

        count=0

        while n:
            if n%2==1:
                count+=1
            n=n//2
        return count 
    
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        
        sum=0
        for i in range(len(nums)):

            if self.setIntegers(i)==k:
                sum+=nums[i]
        return sum