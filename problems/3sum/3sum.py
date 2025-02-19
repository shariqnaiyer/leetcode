class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        start = 0
        end = len(nums) - 1
        while start < end:
            k = start + 1
            print(start, k , end)
            while k < end:
                sumx = nums[start] + nums[end] + nums[k]
                if sumx == 0:
                    po = (nums[start],nums[end],nums[k])
                    res.add(po)
                    k += 1
                    while nums[k] == nums[k-1] and k < end:
                        k += 1
                if sumx > 0:
                    end -= 1
                if sumx < 0:
                    k += 1
            start += 1
            end = len(nums) - 1
        return res
