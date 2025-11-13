class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in s:

            if i == "(" or i == "{" or i == "[":
                l.append(i)

            elif len(l) == 0:
                return False

            elif i == ")":
                x = l.pop()
                if x != "(":
                    return False

            elif i == "}":
                x = l.pop()
                if x != "{":
                    return False

            elif i == "]":
                x = l.pop()
                if x != "[":
                    return False

        if len(l) != 0:
            return False
        
            
        return True