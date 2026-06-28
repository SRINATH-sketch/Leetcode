class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result=[]
        if(k==0):
            return [0]*len(code)
        if(k>0):
            for i in range(len(code)):
                s=0
                for j in range(1,k+1):
                    s=s+code[(i+j)%len(code)]
                result.append(s)
        else:
            k=-k
            for i in range(len(code)):
                s=0
                for j in range(1,k+1):
                    s=s+code[(i-j)%len(code)]
                result.append(s)
        return result