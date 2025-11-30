class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)   
            n >>= 1
        return result & 0xFFFFFFFF

# Example usage:  here >> means right shift and << means left shift

# if n = 34 (which is 00000000000000000000000000100010 in binary)
# The output will be 2684354560 (which is 101000000000000..
# After first iteration: result = 0 | 0 = 0, n = 17 because 34 >> 1 = 17  
# After second iteration: result = 0 | 1 = 1, n = 8
# After third iteration: result = 2 | 0 = 2, n = 4
# After fourth iteration: result = 4 | 0 = 4, n = 2
# After fifth iteration: result = 8 | 0 = 8, n = 1
# After sixth iteration: result = 16 | 1 = 17, n = 000000000000000000000000000 in binary)