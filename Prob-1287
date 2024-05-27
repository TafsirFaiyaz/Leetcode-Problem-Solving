#1287. Element Appearing More Than 25% In Sorted Array

from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        x = Counter(arr)        # This function return a dictionary where it counts how many elements of the same type is in the array.
                                # For example, [4,4,6] it returns counter({ "4" : 2 , "6" : 1})

        for i in x.keys():
            if  x[i] > len(arr)/4:
                return i

# Another solution by me

'''
percent = len(arr) / 4
d = {}

for i in arr:
    if i not in d:        # Checking if i is in the dictionary d. If not then it adds the element. else it increment the value by 1.
        d[i] = 1

    else:
        d[i] += 1

    if d[i] > percent:
        return i
'''
