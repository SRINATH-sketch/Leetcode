class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: abs(x))
        n=len(nums)
        mid=n//2
        ans=0
        for i in range(mid):
            ans-=nums[i]*nums[i]
        for i in range(mid,n):
            ans+=nums[i]*nums[i]
        
        return ans