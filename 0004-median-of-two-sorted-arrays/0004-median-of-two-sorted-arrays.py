class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr=[]

        for i in nums1:
            arr.append(i)
        for i in nums2:
            arr.append(i)

        arr.sort()
        print(arr)
        if len(arr)%2==1:

            x1=len(arr)//2
            print(x1)
            return arr[x1]
        x=arr[len(arr)//2-1]
        y=arr[len(arr)//2]

        print(x,y,len(arr))

        return (x+y)/2