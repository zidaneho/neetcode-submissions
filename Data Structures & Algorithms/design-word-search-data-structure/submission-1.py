class WordDictionary:

    class Node:
        def __init__(self, isEndOfWord = False, neighbors = None):
            self.isEndOfWord = isEndOfWord
            self.neighbors = neighbors if neighbors != None else {}

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.neighbors:
                curr.neighbors[ch] = self.Node()
            curr = curr.neighbors[ch]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        def explore(curr, i):
            if i == len(word) and curr.isEndOfWord:
                return True
            elif i == len(word):
                return False
            ch = word[i]
            if ch == ".":
                for node in curr.neighbors.values():
                    if explore(node, i+1):
                        return True
                return False
            else:
                if ch in curr.neighbors and explore(curr.neighbors[ch],i+1):
                    return True
                else:
                    return False
        return explore(self.root, 0)
            
