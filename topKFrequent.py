class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        k_dict = {}
        for i in nums:
            if i in k_dict:
                k_dict[i] += 1
            else:
                k_dict[i] = 1
        
        res = sorted(k_dict, key=k_dict.get)[::-1]
        return res[0:k]
