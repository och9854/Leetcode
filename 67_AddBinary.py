class Solution:
    def addBinary(self, a: str, b: str) -> str:
       # Pad the strings with 0's on the left to make them the same length
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        # Initialize the carry and result strings
        carry = 0
        result = ''
        
        # Add the digits from right to left
        for i in range(max_len-1, -1, -1):
            digit_sum = carry + int(a[i]) + int(b[i])
            if digit_sum == 0 or digit_sum == 1:
                result = str(digit_sum) + result
                carry = 0
            elif digit_sum == 2:
                result = '0' + result
                carry = 1
            else:  # when digit_sum == 3:
                result = '1' + result
                carry = 1
        
        # If there is a leftover carry digit, add it to the left of the result
        if carry == 1:
            result = '1' + result
        
        return result