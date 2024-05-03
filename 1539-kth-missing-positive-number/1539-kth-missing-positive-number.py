class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        for i in range(1, arr[len(arr)-1]+1):

            if k==0:
                return i-1
            if i not in arr:
                k=k-1
        return i+k