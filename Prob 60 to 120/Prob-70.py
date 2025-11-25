class Solution(object):
    def climbStairs(self, n):               # Fibonacci sequence problem you will understand if you take steps 10 and 20
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        a, b = 1, 2  

        for i in range(3, n + 1):
            b = a + b
            a = b - a   

        return b