class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        teach=0
        for i in hours:
            if(i>=target):
                teach+=1
        return teach