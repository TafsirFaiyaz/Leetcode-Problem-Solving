class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        while n % 3 == 0:           # keep dividing n by 3 while it's divisible
            n //= 3
        return n == 1