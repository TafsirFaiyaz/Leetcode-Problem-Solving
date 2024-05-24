#8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(" ")
        if len(s) < 1:
            return 0

        
        

        if s[0] == "-":

            m="-"
            i=1

        elif s[0] == "+":
            m = ""
            i = 1

        else:

            m = ""
            i=0

        while i<len(s):


            if ord(s[i]) >=48 and ord(s[i]) <= 57:
                m += s[i]

            else:
                break

            i+=1

        
        if m == "" or m == "-":
            return 0

        else:
            m = int(m)

        if m < -2**31:
            m = -(2**31)

        if m > ((2**31) - 1):
            m = ((2**31) - 1)

        return m

  

