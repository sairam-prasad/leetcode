class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        ls =[0]
        rs=[0]

        lsum,rsum=0,0

        for i in range(0,len(nums)-1):
            lsum+=nums[i]
            ls.append(lsum)
        
        j=len(nums)-1

        while(j>0):
            rsum+=nums[j]
            rs.append(rsum)
            j=j-1
        rs=list(reversed(rs))

        answer =[]
        for i in range(len(nums)):
            answer.append(abs(rs[i]-ls[i]))

        return answer