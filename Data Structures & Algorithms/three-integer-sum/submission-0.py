class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        table = {}
        for i,x in enumerate(nums):
            table[x] = i
        triplets = set()
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if i != j:
                    complement = -1 * (x+y)

                    if complement in table and complement + x + y == 0 and i!=j and j!= table[complement] and table[complement] != i:
                        triplets.add(tuple(sorted([x,y,complement])))


        return list(triplets)