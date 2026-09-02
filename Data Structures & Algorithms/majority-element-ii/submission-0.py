class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        result = []
        for key, value in table.items():
            if value > len(nums) // 3:
                result.append(key)
        return result