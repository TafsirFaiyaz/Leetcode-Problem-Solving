#409. Longest Palindrome

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        count = 0
        for i in s:
            if i not in m or m[i] == 0:
                m[i] = 1

            else:
                m[i] = 0
                count += 2

        for val in m.values():
            if val == 1:
                return count + 1

        return count
