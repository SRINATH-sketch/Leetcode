class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = [[]]

        for i in range(len(nums)):
            temp=[]
            for j in result:
                new_arr=j+[nums[i]]
                if(new_arr not in result):
                    temp.append(new_arr)
            result+=temp
        return result