class Solution:
    class Node:
        def __init__(self, new_val):
            self.val = new_val
            self.left = None
            self.right = None
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        combinations = [[]]
        self.dfs(0, nums, [], combinations)
        return combinations
 
    def dfs(self, i, nums, current_combination, combinations):
        if i >= len(nums):
            return
        current_combination.append(nums[i])
        combinations.append(current_combination.copy())
        self.dfs(i+1,nums,current_combination,combinations)
        current_combination.pop()
        self.dfs(i+1,nums,current_combination,combinations)