class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
        visited=set()
        count=0
        def dfs(node):
            visited.add(node)
            for i in range(len(isConnected)):
                if(isConnected[node][i]==1 and i not in visited):
                    dfs(i)

        for i in range(len(isConnected)):
            if(i not in visited):
                count+=1
                dfs(i)

        return count