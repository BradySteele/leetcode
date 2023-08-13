class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        x = len(s)
        for i in range(x-1):
            if romanNumerals[s[i]] < romanNumerals[s[i + 1]]:
                total -= romanNumerals[s[i]]
            else:
                total += romanNumerals[s[i]]
        total += romanNumerals[s[x - 1]]
        return total
            