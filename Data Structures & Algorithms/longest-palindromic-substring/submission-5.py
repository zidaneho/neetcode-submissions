class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalindrome = s[0]
        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                l -= 1
                r += 1
            return s[l+1:r]
        for i in range(len(s)-1):
            odd = expand(i-1,i+1)
            even = expand(i,i+1)
            for card in (odd,even):
                if len(card) > len(maxPalindrome):
                    maxPalindrome = card
        
        return maxPalindrome