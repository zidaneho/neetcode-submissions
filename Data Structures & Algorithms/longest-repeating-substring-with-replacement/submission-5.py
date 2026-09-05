class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        freqs = [0] * 26
        maxFreq = 0
        left = 0
        for right, ch in enumerate(s):
            freqs[ord(ch)-65] += 1
            maxFreq = max(maxFreq,freqs[ord(ch)-65])
            window_size = right - left + 1
            if window_size - maxFreq > k:
                freqs[ord(s[left])-65] -= 1
                left += 1
            maxLength = max(maxLength, right-left+1)
        return maxLength