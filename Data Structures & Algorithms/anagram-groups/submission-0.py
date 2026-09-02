class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for string in strs:
            freqs = {}
            for c in string:
                freqs[c] = freqs[c] + 1 if c in freqs else 1
            groupKey = tuple(sorted(freqs.items()))
            if groupKey in table:
                table[groupKey].append(string)
            else:
                table[groupKey] = [string]
        return list(table.values())
            

