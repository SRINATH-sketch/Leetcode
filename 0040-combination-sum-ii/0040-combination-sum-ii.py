class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def path(index,sum):
            if(index>len(candidates)):
                return
            
            if(sum==target):
                temp=[]
                for i in range(len(candidates)):
                    if(solution[i]=="#"):
                        temp.append(candidates[i])
                arr.append(temp)
                return
            
            if(index==len(candidates)):
                return
            
            if(sum>target):
                return

            solution[index]="#"
            path(index+1,sum+candidates[index])
            solution[index]=0
            next=index+1
            while(next<len(candidates) and candidates[next]==candidates[index]):
                next+=1
            path(next,sum)

        solution=[0]*len(candidates)
        arr=[]
        candidates.sort()
        path(0,0)
        return arr