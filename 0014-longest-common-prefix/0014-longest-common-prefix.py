class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortestString = min(strs)
        prefix = ""
        for i, char in enumerate(shortestString):
            for string in strs:
                if string[i] != char:
                    return prefix
            prefix += char
        return prefix