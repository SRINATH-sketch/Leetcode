class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n=len(gain)
        arr=[]
        for i in range(n+1):
            if(i==0):
                arr.append(i)
            if(i!=0):
                r=arr[i-1]+gain[i-1]
                arr.append(r)
        return max(arr)