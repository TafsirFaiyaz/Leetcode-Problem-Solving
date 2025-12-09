class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = {}
        m = {}
        n = len(s)
        for a,b in zip(s,t):
            if a in l and l[a] != b:
                return False

            if b in m and m[b] != a:
                return False

            l[a] = b
            m[b] = a

        return True 