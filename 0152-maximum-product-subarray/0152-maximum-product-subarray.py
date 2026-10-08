class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product=nums[0]
        min_product=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            current=nums[i]
            a=current
            b=min_product*current
            c=max_product*current

            max_product=max(a,b,c)
            min_product=min(a,b,c)

            ans=max(ans,max_product)
        return ans