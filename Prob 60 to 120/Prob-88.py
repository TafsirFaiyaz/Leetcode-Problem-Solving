class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        l = []

        while i<m and j<n:
            if nums1[i] <= nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1

        while i<m:
            l.append(nums1[i])
            i+=1

        while j<n:
            l.append(nums2[j])
            j+=1

        for i in range(len(l)):
            nums1[i] = l[i]