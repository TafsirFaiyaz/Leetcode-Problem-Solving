class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = [n]
        while n != 1:
            n = str(n)
            x = 0
            for i in range(len(n)):
                x += (int(n[i])) ** 2

            if x in l:
                return False
            l.append(x)
            n = x

        return True