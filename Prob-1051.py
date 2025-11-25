#1051. Height Checker

# The answer is basically checking if the given i'th position of height is exactly in the i'th position of sorted height or not 

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        x = sorted(heights)
        count = 0

        for i in range(len(x)):
            if x[i] != heights[i]:
                count += 1

        return count
        
