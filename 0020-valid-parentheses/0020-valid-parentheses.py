class Solution:
    def isValid(self, s: str) -> bool:
        charDict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for char in s:
            if char in charDict:
                stack.append(char)
            else:
                if not stack or charDict[stack.pop()] != char:
                    return False
        return not stack
        