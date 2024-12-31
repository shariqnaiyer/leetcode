class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        preprod = [1]*len(nums)
        sufprod = [1]*len(nums)
        preprod[0] = 1
        sufprod[n-1] = 1
        for i in range(1,len(nums)):
            preprod[i] = preprod[i-1] * nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            sufprod[j] = sufprod[j+1] * nums[j+1]

        res = []
        for i in range(len(nums)):
            res.append(preprod[i]*sufprod[i])
                    
        return res