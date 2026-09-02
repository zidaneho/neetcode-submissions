class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            success = True
            for c in word:
                if c not in allowed:
                    success = False
                    break
            if success:
                count += 1
        return count