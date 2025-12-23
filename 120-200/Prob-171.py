class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        n = len(columnTitle)
        for i in range(n):
            val = ord(columnTitle[i]) - ord('A') + 1
            result = result * 26 + val
        return result