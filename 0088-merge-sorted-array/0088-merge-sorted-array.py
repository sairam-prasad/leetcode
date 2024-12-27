class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        sum = m+n-1
        m,n=m-1,n-1
        while (m>=0 and n >=0):

            if nums1[m]>nums2[n]:
                nums1[sum] =nums1[m]
                m=m-1
                
            else:
                nums1[sum] =nums2[n]
                n=n-1
            sum=sum-1
            print(m,n)
            print(nums1)
            
        while m>=0:
            nums1[m]=nums1[m]
            m=m-1
        
        while n>=0:
            nums1[n]=nums2[n]
            n=n-1