class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone=0
        for i in jewels:
            for j in range(len(stones)):
                if(i==stones[j]):
                    stone+=1
                    stones[:j]+stones[j+1:]
        return stone