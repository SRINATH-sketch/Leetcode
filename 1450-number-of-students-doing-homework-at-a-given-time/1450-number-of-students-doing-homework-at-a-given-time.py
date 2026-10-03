class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        n=len(startTime)
        count=0
        for i in range(n):
            for j in range(startTime[i],endTime[i]+1):
                if(j==queryTime):
                    count+=1
        return count