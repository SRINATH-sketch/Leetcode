class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c1=0
        l=[]
        for i in nums:
            if(i not in l):
                l.append(i)
                c1+=1
            else:
                continue
        nums[:]=l
        return len(l)