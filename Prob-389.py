class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count1 = {}
        count2 = {}

        for ch in s:
            count1[ch] = count1.get(ch, 0) + 1     # Count characters in s

        for ch in t:
            count2[ch] = count2.get(ch, 0) + 1   # Count characters in t

        for ch in count2:
            if ch not in count1 or count2[ch] > count1[ch]:         # Find the differing character
                return ch
