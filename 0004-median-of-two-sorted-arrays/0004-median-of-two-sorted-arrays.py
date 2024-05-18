class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr=[]
        i,j,m,n= 0,0,len(nums1),len(nums2)

        while i<m and j<n:

            if nums1[i]<=nums2[j]:
                arr.append(nums1[i])
                i=i+1
            elif nums2[j]<nums1[i]:
                arr.append(nums2[j])
                j=j+1

        while i<m:
            arr.append(nums1[i])
            i=i+1

        while j<n:
            arr.append(nums2[j])
            j=j+1
            
        if len(arr)%2==1:
            x1=len(arr)//2
            print(x1)
            return arr[x1]
        x=arr[len(arr)//2-1]
        y=arr[len(arr)//2]

        print(x,y,len(arr))

        return (x+y)/2