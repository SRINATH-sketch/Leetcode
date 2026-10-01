class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        graph={}
        
        for m in range(1,n+1):
            for i in range(1,n+1):
                graph[i]=[]
            for j in range(len(trust)):
                u,v=trust[j]
                graph[u].append(v)

            for k in range(1,n+1):
                c=0
                if(len(graph[k])==0):
                    for i in range(1,n+1):
                        if(k in graph[i]):
                            c+=1

                if(c==n-1):
                    return k
            return -1