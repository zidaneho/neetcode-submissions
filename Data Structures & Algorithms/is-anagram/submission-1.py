class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = {}
        table2 = {}
        for c in s:
            table1[c] = table1[c] + 1 if c in table1 else 1
        for c in t:
            table2[c] = table2[c] + 1 if c in table2 else 1
        return table1 == table2
