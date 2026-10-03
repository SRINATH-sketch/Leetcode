class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        index=[]
        for i in range(len(nums)):
            if(i%10==nums[i]):
                index.append(i)
        if(len(index)>0):
            return min(index)
        return -1