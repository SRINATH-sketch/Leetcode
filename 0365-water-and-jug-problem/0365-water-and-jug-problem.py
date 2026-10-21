from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        queue=deque([])
        visited=set()
        queue.append((0,0))
        visited.add((0,0))

        steps=0
        c=0

        while(queue):
            size=len(queue)
            for i in range(size):
                a,b=queue.popleft()
                if(a==target or b==target):
                    return True
                    c+=1
                    break

                c1=(x,b)
                c2=(a,y)
                c3=(0,b)
                c4=(a,0)
                n=min(a,y-b)
                c5=(a-n,y+n)
                m=min(x-a,b)
                c6=(x+m,b-m)

                arr=[c1,c2,c3,c4,c5,c6]

                for i in arr:
                    if(i not in visited):
                        visited.add(i)
                        queue.append(i)
        
        if(c>0):
            exit()

        return False