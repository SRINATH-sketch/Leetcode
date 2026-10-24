from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        queue=deque([])
        visited=set()
        queue.append((startGene,0))
        visited.add((startGene))

        while queue:
            node,steps=queue.popleft()

            if(node==endGene):
                return steps

            for i in range(len(bank)):
                c=0
                for j in range(len(node)):
                    if(bank[i][j]!=node[j]):
                        c+=1
                if(c==1 and bank[i] not in visited):
                    queue.append((bank[i],steps+1))
                    visited.add((bank[i]))
        
        return -1