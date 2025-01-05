class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        a=[]
        for i in range(len(matrix)):
            b=[]
            j=len(matrix[0])-1

            while j>=0:
                b.append(matrix[j][i])
                j=j-1
            a.append(b)
  

        for i in range(len(a)):
            for j in range(len(a[0])):
                matrix[i][j]=a[i][j]
            