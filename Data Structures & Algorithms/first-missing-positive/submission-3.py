class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        minimum = 1
                    
        for n in nums:
            seen.add(n)
        return self.findMissing(minimum,seen)

    def findMissing(self,num, seen):
        if num not in seen:
            return num
        return self.findMissing(num + 1, seen)