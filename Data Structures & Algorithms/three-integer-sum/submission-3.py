class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        threeSums = []
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    threeSums.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
                
        return threeSums