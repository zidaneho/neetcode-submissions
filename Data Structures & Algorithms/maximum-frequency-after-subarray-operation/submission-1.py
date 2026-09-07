import math
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        max_k = 0
        total_k = 0
        for num in nums:
            if num == k:
                total_k += 1
        for candidate in set(nums):
            curr = 0
            max_curr = -math.inf
            for num in nums:
                if num == candidate:
                    curr += 1
                if num == k:
                    curr -= 1
                max_curr = max(max_curr,curr)
                if curr < 0:
                    curr = 0
            max_k = max(max_curr + total_k,max_k)
        return max_k
           

                
