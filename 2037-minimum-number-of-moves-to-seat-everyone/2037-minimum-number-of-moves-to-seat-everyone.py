class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        sums=0
        for i in range(len(seats)):
            sums+=abs(seats[i]-students[i])
        return sums