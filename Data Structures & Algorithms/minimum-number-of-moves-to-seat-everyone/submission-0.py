class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        moves = 0
        for i in range(len(students)):
            student = students[i]
            seat = seats[i]
            moves += abs(student-seat)
        return moves
