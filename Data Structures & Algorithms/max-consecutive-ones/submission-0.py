class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                if curr > maxOnes:
                    maxOnes = curr
            elif num == 0:
                curr = 0
        return maxOnes