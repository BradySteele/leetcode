class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        combos = [0] * (n + 1)
        combos[0] = combos[1] = 1
        
        for i in range(2, n + 1):
            combos[i] = combos[i -1] + combos[i - 2]
            
        return combos[i]