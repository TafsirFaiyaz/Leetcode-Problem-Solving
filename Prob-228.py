class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        strt = nums[0]
        end = nums[0]
        output = []

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if strt == end:
                    output.append(str(strt))
                else:
                    output.append(str(strt) + "->" + str(end))
                strt = nums[i]
                end = nums[i]

        if strt == end:
            output.append(str(strt))
        else:
            output.append(str(strt) + "->" + str(end))

        return output