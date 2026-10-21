class TimeMap:

    def __init__(self):
        self.data={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.data):
            self.data[key]=[]
        return self.data[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.data):
            return ""
        
        arr=self.data[key]
        left=0
        right=len(arr)-1
        ans=""
        
        while left<=right:
            mid=(left+right)//2
            if(arr[mid][0]<=timestamp):
                ans=arr[mid][1]
                left=mid+1
            else:
                right=mid-1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)