class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows<2:
            return [[1]]

        res = [[1]]
        for i in range(2,numRows+1):
            l = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    l.append(1)
                else:
                    l.append(res[-1][j-1] + res[-1][j])

            res.append(l)

        return res