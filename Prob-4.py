# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x=[]
        x=nums1+nums2
        x.sort()        # Merging and sorting the array

        if len(x)%2==0:    # Checking if the length of array is even or odd

            return (( x[len(x) // 2] + x[(len(x) // 2) - 1] ) / 2)
        else:

            return x[len(x) // 2]

        
