class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        sums=float('inf')
        for i in range(n-2):
            l=i+1
            r=n-1
            while(l<r):
                csum=nums[l]+nums[r]+nums[i]
                if(abs(csum-target)<abs(sums-target)):
                    sums=csum
                if(csum<target):
                    l+=1
                elif(csum>target):
                    r-=1
                else:
                    return csum
        return sums