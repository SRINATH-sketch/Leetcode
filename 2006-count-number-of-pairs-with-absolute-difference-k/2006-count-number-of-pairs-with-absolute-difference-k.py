class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            for j in range(n):
                if(i!=j and nums[i]-nums[j]==k):
                    c+=1
        
        return c