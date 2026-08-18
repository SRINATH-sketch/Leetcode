class Solution:
    m=1
    def arraySign(self, nums: List[int]) -> int:
        m=1
        def signFunc(x):
            if(x>0):
                return 1
            elif(x<0):
                return -1
            else:
                return 0
        for i in nums:
            m*=i
        return signFunc(m)