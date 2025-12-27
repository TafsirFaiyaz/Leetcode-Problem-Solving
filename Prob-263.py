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
            while n % i == 0:
                n //= i

        return n == 1