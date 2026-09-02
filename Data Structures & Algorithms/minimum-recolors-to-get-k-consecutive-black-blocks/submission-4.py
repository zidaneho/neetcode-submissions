class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        window = 0
        for i in range(k):
            if blocks[i] == 'W':
                window += 1
        minWhites = window

        firstIdx = 0
        lastIdx = k-1
        while lastIdx < len(blocks)-1:
            
            
            
            firstBlock = 1 if blocks[firstIdx] == "W" else 0
            firstIdx += 1
            lastIdx += 1
            lastBlock = 1 if blocks[lastIdx] == "W" else 0
            window += lastBlock - firstBlock
            if window < minWhites:
                minWhites = window
        return minWhites
