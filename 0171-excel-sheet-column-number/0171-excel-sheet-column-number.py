class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        result = 0
        
        for i in range(len(columnTitle)):
            char = columnTitle[i]
            charValue = ord(char) - ord('A') + 1
            power = len(columnTitle) - i - 1
            result += charValue * (26 ** power)
            
        return result
        