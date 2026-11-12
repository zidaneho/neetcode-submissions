class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs = {}
        for ch in t:
            freqs[ch] = freqs.get(ch,0) + 1
        
        windowFreqs = {}
        minWindow = float('inf')
        resL = 0
        resR = -1
        l = 0
        def isValidWindow():
            for ch in freqs.keys():
                if ch not in windowFreqs or freqs[ch] > windowFreqs[ch]:
                    return False
            return True
        for r, ch in enumerate(s):
            windowFreqs[ch] = windowFreqs.get(ch, 0) + 1
            while l <= r and s[l] in windowFreqs and windowFreqs[s[l]] - 1 >= freqs.get(s[l], -float('inf')):
                windowFreqs[s[l]] -= 1
                l += 1
            if r - l + 1 < minWindow and isValidWindow():
                resL = l
                resR = r
                minWindow = r - l + 1
        return s[resL:resR+1]
        