class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        coun=0
        for i in set(nums):
            if(nums.count(i)==3):
                index=[]
                for j in range(len(nums)):
                    if(nums[j]==i):
                        index.append(j)
                if(index[1]-index[0] == index[2]-index[1]):
                    coun+=1
        return coun