class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        maxi = arr[len(arr)-1]
        arr[len(arr)-1]= -1
        temp_max=0

        
        for i in range(len(arr)-2,-1,-1):
            
            if arr[i]>maxi:
                temp_max = maxi
                maxi= arr[i]
                arr[i]=temp_max

            else:
                arr[i]=maxi
            
        #arr[len(arr)-1]=-1

        return arr
                
        