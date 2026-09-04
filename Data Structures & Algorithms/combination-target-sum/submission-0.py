class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        nums = sorted(nums)
        def write_combinations(curr_sum, curr_list, index):
            if curr_sum  == target:
                combinations.append(curr_list.copy())
                return
            elif curr_sum > target:
                return
            
            while index < len(nums):
                curr_sum += nums[index]
                curr_list.append(nums[index])
                write_combinations(curr_sum,curr_list,index)
                curr_list.pop()
                curr_sum -= nums[index]
                index += 1
        write_combinations(0,[],0)
        return combinations