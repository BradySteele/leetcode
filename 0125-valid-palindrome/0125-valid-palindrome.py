class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = re.sub(r'[\W_]', '', s.lower())
        
        return i == i[::-1]