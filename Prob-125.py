class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        text = s.lower()
        result = re.sub(r'[^A-Za-z0-9]', '', text)     # Remove non-alphanumeric characters
        n = len(result)
        
        for i in range(n//2):
            if result[i] != result[n-1-i]:
                return False
            
        return True