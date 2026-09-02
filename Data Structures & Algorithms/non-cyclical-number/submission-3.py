class Solution:
    squaredTable = {
            0 : 0,
            1 : 1,
            2: 4,
            3: 9,
            4: 16,
            5: 25,
            6: 36,
            7: 49,
            8: 64,
            9: 81,
        }
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while True:
            n = self.calculate(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
        return False
    def calculate(self, n: int):
        total = 0
        while n != 0:
            digit = n % 10
            total += self.squaredTable[digit]
            n = n // 10
        return total
    
