class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(nums):
            arr = [0] * (len(nums) + 1)
            arr[-1] = 0
            arr[-2] = nums[-1]
        
            for i in range(len(nums)-2,-1,-1):
                if i == 0:
                    arr[i] = max(nums[i] + arr[i+2],arr[i+1])
                else:
                    arr[i] = max(nums[i] + arr[i+2],arr[i+1])
            return arr[0]
        return max(rob_line(nums[0:-1]),rob_line(nums[1:]))
        