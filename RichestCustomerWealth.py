class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=0
        for i in accounts:
            s=0
            for j in i:
                s+=j
            if(s>max):
                max=s
        return max