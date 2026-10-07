class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        c=0

        for i in range(n-1,1,-1):
            l=nums[i]
            left=0
            right=i-1

            while(left<right):
                if(nums[left]+nums[right]>l):
                    c+=right-left
                    right-=1
                else:
                    left+=1
        return c