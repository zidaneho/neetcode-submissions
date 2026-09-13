class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            idx = magazine.find(ch)
            if idx != -1:
                magazine = magazine[0:idx] + magazine[idx+1:]
            else:
                return False
        return True