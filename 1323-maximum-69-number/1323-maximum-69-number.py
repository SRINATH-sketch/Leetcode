class Solution:
    def maximum69Number (self, num: int) -> int:
        arr1=[]
        for i in range(len(str(num))):
            arr=[]
            m=str(num)
            for j in range(len(str(num))):
                if(j==i):
                    if(m[j]=='6'):
                        arr.append('9')
                    elif(m[j]=='9'):
                        arr.append('9')
                else:
                    arr.append(m[j])
            arr1.append(int("".join(arr)))
        return max(arr1)