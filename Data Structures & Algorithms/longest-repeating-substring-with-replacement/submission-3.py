from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapping = {}
        maxFreq = 0
        left = 0
        result = 0
        for i in range(len(s)):
            if s[i] in mapping:
                mapping[s[i]] += 1
            else:
                mapping[s[i]] = 1
            maxFreq = max(maxFreq, mapping[s[i]])
            while (i - left + 1) - maxFreq > k:
                mapping[s[left]] -= 1
                left += 1
            result = max(result, i - left + 1)
        return result

        