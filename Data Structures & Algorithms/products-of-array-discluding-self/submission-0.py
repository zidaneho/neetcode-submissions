class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        result = []
        product = 1
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num
        if zeroCount > 1:
            for num in nums:
                result.append(0)
            return result
        for num in nums:
            if num == 0:
                result.append(product)
            elif zeroCount > 0:
                result.append(0)
            else:
                result.append(product // num)
        return result
        