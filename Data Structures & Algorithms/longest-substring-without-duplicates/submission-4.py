class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ""
        index = 0
        longestWindow = 0
        while index < len(s):
            if s[index] in window:
                window = window[window.index(s[index])+1:] + s[index]
            else:
                window += s[index]
            index += 1
            if len(window) > longestWindow:
                    longestWindow = len(window)
        return longestWindow