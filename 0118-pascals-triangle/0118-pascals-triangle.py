class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        
        triangle = [[1]]
        
        for i in range(1, numRows):
            prevRow = triangle[i - 1]
            newRow = [1]
            
            for j in range(1, i):
                newRow.append(prevRow[j - 1] + prevRow[j])
                
            newRow.append(1)
            triangle.append(newRow)
        
        return triangle