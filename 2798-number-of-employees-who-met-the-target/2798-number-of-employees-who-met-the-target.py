class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        count=0
        for i in range(len(hours)):
            if target<=hours[i]:
                count+=1

        return count
