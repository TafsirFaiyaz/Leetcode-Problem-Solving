class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        if n % 2 != 0 or 2 > n:          # If n is odd and not 1, it cannot be a power of two. Also if n is less than 2, it cannot be a power of two.
            return False

        i = 1
        while i<=32:     # Limit to avoid infinite loop for large n as constraints were 2**31
            x = 2 ** i
            i+=1
            if x == n:
                return True 
            
        return False    # If no power of two matches n, return False
    
    
'''
Best Solution:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        
    # Explanation:
    # A power of two in binary representation has exactly one bit set to 1. So, when we subtract 1 from a power of two, all the bits after the set bit become 1s and the set bit becomes 0.
    # For example:
    # 4 (which is 2^2) in binary is 100
    # 3 (which is 4-1) in binary is 011
    # Performing a bitwise AND between 4 and 3 gives us 0 (100 & 011 = 000).
    # Thus, if n is a power of two, n & (n - 1) will be 0.
'''