class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if words:
            lastWord = words[-1]
            return len(lastWord)