import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_curr = -math.inf
        for num in nums:
            curr += num
            max_curr = max(curr,max_curr)
            if curr < 0:
                curr = 0
        return max_curr