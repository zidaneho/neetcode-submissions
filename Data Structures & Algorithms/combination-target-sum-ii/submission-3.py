class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def explore(index, current_arr, target):
            if target == 0:
                res.append(current_arr[:])
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                num = candidates[i]
                if num > target:
                    break
                current_arr.append(num)
                explore(i+1, current_arr, target-num)
                current_arr.pop()
        explore(0, [],target)
        return res
