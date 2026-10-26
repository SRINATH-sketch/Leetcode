from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
    
        for i in range(n):
            if(color[i]==-1):
                queue=deque([i])
                color[i]=0

                while queue:
                    node=queue.popleft()

                    for i in graph[node]:
                        if(color[i]==-1):
                            color[i]=1-color[node]
                            queue.append(i)
                        elif(color[i]==color[node]):
                            return False
        return True