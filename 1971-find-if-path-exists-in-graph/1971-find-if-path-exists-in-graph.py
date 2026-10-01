from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph={}
        for i in range(n):
            graph[i]=[]
        for j in edges:
            u,v=j
            graph[u].append(v)
            graph[v].append(u)

        queue=deque([source])
        visited=set()

        while(queue):
            node=queue.popleft()
            if(node in visited):
                continue
            if(node==destination):
                return True
            visited.add(node)
            for i in graph[node]:
                queue.append(i)
        return False