class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        total = 0
        for c in set(s):
            index1 = s.find(c)
            index2 = s.rfind(c)
            if index2 - index1 > 1:
                total += len(set(s[index1+1:index2]))
        return total
