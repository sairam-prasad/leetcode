class Solution:

    def reverse_array(self, i,j,nums):

        while(i<j):
            nums[i],nums[j]=nums[j],nums[i]
            i=i+1
            j=j-1
        return nums

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        break_point,element=0,0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                break_point= i
                flag = True
                break
        print(nums[break_point])
        n=len(nums)-1

        while(n>break_point):
            
            if nums[n]>nums[break_point]:
                element = n
                break
            n=n-1 

        print(nums[element])
        print(nums)
        nums[break_point], nums[element] = nums[element], nums[break_point]

        print(nums)
        if flag == True:   
            nums=self.reverse_array(break_point+1,len(nums)-1,nums)
        else:
            nums=self.reverse_array(0,len(nums)-1,nums)

        
        