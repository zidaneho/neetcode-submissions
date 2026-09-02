class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 1
        num = 0
        while i <= len(nums):
            num += i
            i += 1
        return num - sum(nums)
          