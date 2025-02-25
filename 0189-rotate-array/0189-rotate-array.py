class Solution:

    def reverse(self, nums, i,j):

        while i<=j:
            nums[i],nums[j]= nums[j],nums[i]
            i=i+1
            j=j-1
        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums = self.reverse(nums, 0,len(nums)-1)
        nums= self.reverse(nums, 0,k-1)
        nums= self.reverse(nums,k, len(nums)-1)

        