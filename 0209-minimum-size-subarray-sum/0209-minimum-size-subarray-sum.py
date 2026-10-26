class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        s=0
        left=0
        n=len(nums)
        r=float('inf')
        for i in range(n):
            s+=nums[i]
            while(s>=target):
                r=min(r,i-left+1)
                s-=nums[left]
                left+=1
        if(r!=float('inf')):
            return r
        return 0