class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        n=len(nums)
        for i in range(n):
            left=nums[:i]
            right=nums[i+1:]
            
            if(sum(left)==sum(right)):
                return i
        return -1