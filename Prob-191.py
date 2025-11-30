class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = str(bin(n))
        count = 0
        for i in range(len(x)):
            if x[i] == '1':
                count+=1

        return count
        
        