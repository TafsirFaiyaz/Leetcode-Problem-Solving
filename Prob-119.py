class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 1:
            return [1]

        res = [[1]]
        for i in range(1,rowIndex+1):
            l = [1]*(i+1)
            for j in range(1,i):
                l[j] = res[0][j-1] + res[0][j]

            res[0] = l
        return res[0]        