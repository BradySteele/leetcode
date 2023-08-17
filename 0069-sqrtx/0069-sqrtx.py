class Solution:
    def mySqrt(self, x: int) -> int:
        e = x
        b = 0

        result = x
        while (b <= e):
            m = int(b + (e - b) // 2)
            
            if (m * m) == x:
                return m
            elif (m * m) > x:
                e = m -1
            else:
                result = m
                b = m + 1
                
        return result