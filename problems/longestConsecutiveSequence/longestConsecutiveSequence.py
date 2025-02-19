class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        maxi = 0
        nums = set(nums)

        for i in nums:
            if i - 1 not in nums:
                p = i
                while p in nums:
                    p = p + 1

                maxi = max(maxi, p - i)
            
        return maxi