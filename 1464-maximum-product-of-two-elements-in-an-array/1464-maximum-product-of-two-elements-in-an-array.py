class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        arr=[]
        for i in range(n):
            for j in range(n):
                if(i!=j):
                    num=(nums[i]-1)*(nums[j]-1)
                    arr.append(num)
        return max(arr)