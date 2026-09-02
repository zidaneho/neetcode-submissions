class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        maxLength = 0
        for num in table:
            if num-1 not in table:
                length = 1
                while num + length in table:
                    length += 1
                if maxLength < length:
                    maxLength = length
        return maxLength
