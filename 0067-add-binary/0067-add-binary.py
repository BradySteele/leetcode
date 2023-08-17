class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []                         # Initialize an empty list to store the binary sum
        carry = 0                           # Initialize the carry to 0
        i, j = len(a) - 1, len(b) - 1       # Initialize pointers to the rightmost digits of a and b
        
        while i >= 0 or j >= 0 or carry:    # Continue the loop until digits and carry are exhausted
            sum_ = carry                    # Initialize the sum with the current carry
            
            if i >= 0:                      # If there are digits left in a
                sum_ += int(a[i])           # Add the current digit of a to sum
                i -= 1                      # Move the pointer to the next digit of a
            
            if j >= 0:                      # If there are digits left in b
                sum_ += int(b[j])           # Add the current digit of b to sum
                j -= 1                      # Move the pointer to the next digit of b
            
            result.append(str(sum_ % 2))    # Append the current binary digit to result
            carry = sum_ // 2               # Calculate the new carry
            
        return ''.join(result[::-1])        # Join the binary digits in reverse order to get the final sum
