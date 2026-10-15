class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        maxRes = nums[0]
        index = 1
        while index < len(nums):
            candidates = [nums[index], nums[index] * curMax, nums[index] * curMin]
            curMax = max(candidates)
            curMin = min(candidates)
            index += 1
            maxRes = max(curMax, maxRes)
        
        return maxRes
