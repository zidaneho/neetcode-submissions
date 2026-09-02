class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []
        for i in range(32):
            stack.append(n & 1)
            n = n>>1
        reversed_int = 0
        while len(stack) > 0:
            bit = stack.pop(0)
            reversed_int = reversed_int | bit
            reversed_int = reversed_int << 1
        reversed_int = reversed_int >> 1
        return reversed_int