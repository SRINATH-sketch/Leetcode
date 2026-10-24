class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        dict={}
        day=0
        for i in tasks:
            day+=1
            if(i in dict):
                day=max(day,dict[i]+space+1)

            dict[i]=day
        return day