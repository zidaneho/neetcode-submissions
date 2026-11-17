class Solution:
    def countSubstrings(self, s: str) -> int:
        def explore(l,r):
            if l < 0 or r >= len(s):
                return 0
            if s[l] == s[r]:
                return 1 + explore(l-1,r+1)
            return 0
        total = 0
        for i in range(len(s)):
            total += explore(i,i) + explore(i,i+1)
        return total
            
            