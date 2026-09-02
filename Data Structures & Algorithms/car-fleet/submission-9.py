class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position,speed))
        position, speed = map(list, zip(*sorted_pairs))
        stack = []
        for i in range(len(position)-1,-1,-1):
            stack.append((target - position[i]) / speed[i])
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)