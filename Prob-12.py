#12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        
        x=int(num)
        s=""
        n=x
        while x>3:

            n=x
            if x//1000!=0:    # Checks for thousands. If x is 1000 or more, it appends "M" for each thousand
                x=x%1000      
                n=n//1000     # Counting how many M we have to append
                s+="M"*n

            elif x//900!=0:
                x=x%900
                n=n//900
                s+="CM"*n

            elif x//500!=0:
                x=x%500
                n=n//500
                s+="D"*n

            elif x//400!=0:
                x=x%400
                n=n//400
                s+="CD"*n

            elif x//100!=0:
                x=x%100
                n=n//100
                s+="C"*n


            elif x//90!=0:
                x=x%90
                n=n//90
                s+="XC"*n

            elif x//50!=0:
                x=x%50
                n=n//50
                s+="L"*n

            elif x//40!=0:
                x=x%40
                n=n//40
                s+="XL"*n

            elif x//10!=0:
                x=x%10
                n=n//10
                s+="X"*n

            elif x//9!=0:
                x=x%9
                n=n//9
                s+="IX"*n

            elif x//5!=0:
                x=x%5
                n=n//5
                s+="V"*n

            elif x//4!=0:
                x=x%4
                n=n//4
                s+="IV"*n
            

        s+="I"*x       # If x still not 0 then it appends "I" x times at the end of the string 
        return s
