class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefixes = 0
        for word in words:
            index = word.find(pref)
            if index == 0:
                prefixes += 1
        return prefixes