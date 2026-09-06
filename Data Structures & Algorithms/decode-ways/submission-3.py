from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        self.decodings = 0
        @lru_cache(maxsize=None)
        def traverse(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            
            decodings = traverse(index+1)

            num1 = int(s[index])
            if index + 1 < len(s):
                num2 = num1 * 10 + int(s[index+1])
                if num2 <= 26 and num2 >= 10:
                    decodings += traverse(index+2)
            return decodings
        return traverse(0)
            
