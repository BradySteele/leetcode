class Solution:
    def isPalindrome(self, x: int) -> bool:
        strValue = str(x)
        reversedValue = strValue[::-1]
        if reversedValue == strValue:
            return True
        return False