class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(n):
                if(i<j):
                    if(i!=j and (nums[i]+nums[j])<target):
                        count+=1
        return count