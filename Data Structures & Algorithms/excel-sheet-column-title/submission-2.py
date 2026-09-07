class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        digit = columnNumber % 10
        res = 0
        title = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            title += chr(65 + remainder)
            columnNumber //= 26
        return title[::-1]