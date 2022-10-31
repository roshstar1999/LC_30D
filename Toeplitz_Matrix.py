class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        minl=min(len(matrix),len(matrix[0]))
        x=len(matrix[0])
        for i in range(len(matrix)-1):
            if matrix[i][:x-1]!=matrix[i+1][1:]:
                return False
        return True
                
        '''
        for i in range(0,minl):
            if x!=matrix[i][i]:
                return False
        return True
            
        '''
