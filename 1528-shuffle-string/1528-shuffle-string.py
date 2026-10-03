class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        new_string=""
        for i in range(len(s)):
            for j in range(len(indices)):
                if(i==indices[j]):
                    new_string+=s[j]
        return new_string