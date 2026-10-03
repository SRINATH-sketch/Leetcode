class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        index=[]
        for i in range(len(nums)):
            b=bin(i)[2:]
            c=0
            for j in str(b):
                if(j=='1'):
                    c+=1
            if(c==k):
                index.append(i)
        s=0
        for i in index:
            s+=nums[i]
        return s