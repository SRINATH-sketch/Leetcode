from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph=[[] for i in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue=deque([])
        visited=set()

        queue.append((source))
        visited.add((source))

        while queue:
            node=queue.popleft()

            if(node==destination):
                return True

            for i in graph[node]:
                if(i not in visited):
                    visited.add((i))
                    queue.append((i))
        
        return False