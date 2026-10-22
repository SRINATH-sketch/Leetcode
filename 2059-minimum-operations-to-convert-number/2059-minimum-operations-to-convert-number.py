from collections import deque
class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        queue=deque([])
        visited=set()
        queue.append((start,0))
        visited.add((start))

        while queue:
            num,steps=queue.popleft()

            if(num==goal):
                return steps

            for j in nums:
                for i in [num+j,num-j,num^j]:

                    if i==goal:
                        return steps+1

                    if((i>=0 and i<=1000) and i not in visited):
                        visited.add((i))
                        queue.append((i,steps+1))
        
        return -1