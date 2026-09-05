class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            if len(word) < len(prefix):
                prefix = word
        
        
        for i in range(1,len(strs)):
            word = strs[i]
            j = 0
            newPrefix = ""
            
            while j < len(prefix) and prefix[j] == word[j]:
                newPrefix += prefix[j]
                j += 1
            prefix = newPrefix
        return prefix
        
