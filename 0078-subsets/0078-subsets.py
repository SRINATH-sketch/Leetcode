class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def path(index):
            if(index>len(nums)):
                return
            
            if(index==len(nums)):
                arr1.append(arr[:])
                return
            
            if(index==len(nums)):
                return

            arr.append(nums[index])
            path(index+1)

            arr.pop()
            path(index+1)

        arr=[]
        arr1=[]
        path(0)
        return arr1