from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
            queue=deque([])
            queue.append((0,[0]))
            n=len(graph)
            paths=[]
            while(queue):
                node,path=queue.popleft()

                if(node==n-1):
                    paths.append(path)

                for i in graph[node]:
                    queue.append((i,path+[i]))
            return paths