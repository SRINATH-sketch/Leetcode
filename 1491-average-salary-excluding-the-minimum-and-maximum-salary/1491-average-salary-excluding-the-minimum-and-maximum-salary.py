class Solution:
    def average(self, salary: list[int]) -> float:
        mini=min(salary)
        maxi=max(salary)
        s=0
        count=0
        for i in salary:
            if(i!=mini and i!=maxi):
                s+=i
                count+=1
        return s/count