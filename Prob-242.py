class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_string = ''.join(sorted(t))
        sorted_string2 = ''.join(sorted(s))
        return sorted_string2 == sorted_string
        