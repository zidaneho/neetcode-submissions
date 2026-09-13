class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ranks = {}
        i = 0
        for ch in order:
            ranks[ch] = i
            i += 1
        
        if len(words) == 1:
            return True

        for i in range(len(words)-1):
            word1 =  words[i]
            word2 = words[i+1]
            j = 0
            matched = True
            while j < len(word1) and j < len(word2):
                if ranks[word1[j]] != ranks[word2[j]]:
                    if ranks[word1[j]] > ranks[word2[j]]:
                        return False
                    matched = False
                    break
                j += 1
            if matched and len(word1) > len(word2):
                return False
               
        return True
