class Solution:
    def romanToInt(self, s: str) -> int:
        s += " "
        self.sum=0

        for i in range(len(s) - 1):
            y=0

            if s[i]=="I" and s[i+1]=="V":       #Checking if the strings i'th and i+1'th element is "IV"
                y=-1
                                                # Reducing -1 because "IV" = 4 but when the i will increase the next value would be "V" = 5. 
                                                # So ultimately sum will result in 5-1 = 4  

            elif s[i]=="I" and s[i+1]=="X":    # Checking if it is "IX"
                y=-1

            elif s[i]=="X" and s[i+1]=="L":
                y=-10
            elif s[i]=="X" and s[i+1]=="C":
                y=-10

            elif s[i]=="C" and s[i+1]=="D":
                y=-100
            elif s[i]=="C" and s[i+1]=="M":
                y=-100

            elif s[i]=="I":
                y=1
            elif s[i]=="V":
                y=5

            elif s[i]=="X":
                y=10
            elif s[i]=="L":
                y=50

            elif s[i]=="C":
                y=100
            elif s[i]=="D":
                y=500

            elif s[i]=="M":
                y=1000

            self.sum+=y

        return self.sum

            
