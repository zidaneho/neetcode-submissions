class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            word = words[i]
            print("h",word)
            for j in range(len(words)):
                if len(words[j]) < len(word) or i == j:
                    continue
                index = words[j].find(word)
                
                if index != -1:
                    result.append(word)
                    break
        return result