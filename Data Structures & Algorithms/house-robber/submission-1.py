class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0] * (len(nums) + 1)
        arr[-1] = 0
        arr[-2] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            arr[i] = max(nums[i] + arr[i+2],arr[i+1])
        return arr[0]

