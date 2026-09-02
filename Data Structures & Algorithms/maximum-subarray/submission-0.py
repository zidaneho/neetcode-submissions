class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum = -10001
        currSum = 0
        for num in nums:
            if currSum + num < num:
                currSum = num
            else:
                currSum += num
            if largestSum < currSum:
                largestSum = currSum
   
        return largestSum
                