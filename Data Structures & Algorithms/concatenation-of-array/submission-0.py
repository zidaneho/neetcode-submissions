class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = nums.copy()
        nums.extend(arr)

        return nums