class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapping2 = {}
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            print(char1,char2,mapping.get(char1,"none"))
            if char1 in mapping and mapping[char1] != char2:
                return False
            if char2 in mapping2 and mapping2[char2] != char1:
                return False
            
            mapping[char1] = char2
            mapping2[char2] = char1
        return True
