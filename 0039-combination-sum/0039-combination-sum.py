class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def path(index,sum):
            if(index>=len(candidates)):
                return

            if(sum==target):
                arr1.append(arr[:])
                return
            
            if(sum>target):
                return

            if(index==len(candidates)):
                return 

            arr.append(candidates[index])
            path(index,sum+candidates[index])
            arr.pop()

            path(index+1,sum)

        arr1=[]
        arr=[]
        path(0,0)
        return arr1