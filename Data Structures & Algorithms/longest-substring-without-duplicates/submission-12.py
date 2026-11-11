class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindowSize = 0
        table = {}
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        table[s[left]] = 1
        while right < len(s):
            if s[right] not in table:
                table[s[right]] = 0
            table[s[right]] += 1
            while table[s[right]] > 1:
                table[s[left]] -= 1
                left += 1
              
            maxWindowSize = max(maxWindowSize, right - left + 1)
            right += 1

        return maxWindowSize