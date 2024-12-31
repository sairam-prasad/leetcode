class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict={}
        
        for i in range(0,len(nums)):
            
            if dict.get(nums[i]):
                dict[nums[i]]=dict.get(nums[i])+1
            else:
                dict[nums[i]]=1
        
        a=0
        print(dict)
        for i,j in dict.items():
            print(i,j)
            if j>a:
                max=i
                a=j
        return max

            
            
        