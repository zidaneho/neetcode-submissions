class PrefixTree:

    class Node:
        def __init__(self,isEndOfWord = False, neighbors = None):
            self.neighbors = neighbors if neighbors != None else {}
            self.isEndOfWord = isEndOfWord

    def __init__(self):
        self.root = self.Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.neighbors:
                curr.neighbors[ch] = self.Node()
            curr = curr.neighbors[ch]
        curr.isEndOfWord = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.neighbors:
                return False
            curr = curr.neighbors[ch]
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.neighbors:
                return False
            curr = curr.neighbors[ch]
        return True
        