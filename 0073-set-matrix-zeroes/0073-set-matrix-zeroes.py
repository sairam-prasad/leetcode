class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m= len(matrix)
        n=len(matrix[0])

        row = [0]*n
        col = [0]*m
        print(row,col)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[j]=1
                    col[i]=1
        print(row)
        print(col)
        for i in range(m):
            for j in range(n):
                if row[j] or col[i]:
                    matrix[i][j]=0