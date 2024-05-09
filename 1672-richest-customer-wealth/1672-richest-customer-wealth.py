class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        


        maximum=0
        for i in range(len(accounts)):
            sum=0

            for j in range(len(accounts[0])):
                sum+=accounts[i][j]
            
            maximum=max(sum,maximum)
            print(sum,maximum)
        return maximum
