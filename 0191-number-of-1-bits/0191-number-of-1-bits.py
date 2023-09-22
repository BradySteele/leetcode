class Solution:
    def hammingWeight(self, n: int) -> int:
        
        binary = bin(n)
        hamming = 0
        
        for bit in binary:
            if bit == '1':
                hamming += 1
                
        return hamming