class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        result = []

        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result.append(letters[remainder])
            columnNumber //= 26

        return ''.join(reversed(result))
        