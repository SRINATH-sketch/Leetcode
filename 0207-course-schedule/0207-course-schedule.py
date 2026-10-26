from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph=[[] for i in range(numCourses)]
        indegree=[0]*numCourses

        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1

        queue=deque([])
        for i in range(numCourses):
            if(indegree[i]==0):
                queue.append(i)
        count=0
        while queue:
            node=queue.popleft()
            count+=1
            for i in graph[node]:
                indegree[i]-=1
                if(indegree[i]==0):
                    queue.append(i)
        return count==numCourses