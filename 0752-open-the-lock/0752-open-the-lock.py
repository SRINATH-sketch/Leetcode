from collections import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        queue=deque([])
        visited=set()
        steps=0
        start=(0,0,0,0)
        queue.append((start))
        visited.add((start))

        if("0000" in deadends):
            return -1

        while(queue):
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                w1,w2,w3,w4=node   
                node="".join(map(str,node)) 
                if(node==target):
                    return steps

                c1=(w1+1)%10,w2,w3,w4
                c2=(w1-1)%10,w2,w3,w4
                c3=w1,(w2+1)%10,w3,w4
                c4=w1,(w2-1)%10,w3,w4
                c5=w1,w2,(w3+1)%10,w4
                c6=w1,w2,(w3-1)%10,w4
                c7=w1,w2,w3,(w4+1)%10
                c8=w1,w2,w3,(w4-1)%10

                arr=[c1,c2,c3,c4,c5,c6,c7,c8]

                for i in arr:
                    if("".join(map(str,i)) not in deadends and i not in visited):
                        visited.add(i)
                        queue.append(i)
            steps+=1
        return -1