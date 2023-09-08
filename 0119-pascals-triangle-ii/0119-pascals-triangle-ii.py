class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]

        prevRow = [1]

        for i in range(1, rowIndex + 1):
            nextRow = [1]
            for j in range(1, i):
                nextNum = prevRow[j - 1] + prevRow[j]
                nextRow.append(nextNum)
            nextRow.append(1)

            prevRow = nextRow

        return prevRow