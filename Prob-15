#15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = set()    # Because we don't want duplicate values in the result
        
        for i in range(len(nums)-2):

            m = nums[i]         # i'th num is fixed 
            j = i + 1
            k = len(nums)-1

            while j < k:        # Searching for j and k so that we can get the sum of i, j and k is 0
                n = nums[j]
                o = nums[k]

                target = m + n + o   

                if target > 0:       # If target is greater than zero we are reducing the value of k as nums is sorted and value of k'th element is the reason target value is greater than zero 
                    k -= 1

                elif target < 0:     # If target is greater than zero we are reducing the value of j as nums is sorted and value of j'th element is the reason target value is lesser than zero 
                    j += 1

                else:
                    result.add((m,n,o))    # If the target is zero we got one of our resultant value. If the value already exist in the result then it won't be added as result is a set

                    j += 1             # Reducing k and increasing j because we don't want to stuck in infinite while loop
                    k -= 1

        return result
