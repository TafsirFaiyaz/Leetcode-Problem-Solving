class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n < 1:
            return False

        z = (2, 3, 5)

        for i in z:
            while n % i == 0:    # keep dividing n by i while n is divisible by i
                n //= i

        return n == 1           # if n is reduced to 1, then n is an ugly number else not 
    
    
# n = 8
# n //= 2  # 4
# n //= 2  # 2
# n //= 2  # 1    # So, n is ugly number