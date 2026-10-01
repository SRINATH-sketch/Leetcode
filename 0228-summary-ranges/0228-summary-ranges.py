class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        i=0
        arr=[]
        while(i<len(nums)):
            j=i

            while(j+1<len(nums) and nums[j]+1==nums[j+1]):
                j+=1
            
            if(i==j):
                arr.append(str(nums[j]))
            else:
                arr.append(str(nums[i])+"->"+str(nums[j]))
            i=j+1
        return arr