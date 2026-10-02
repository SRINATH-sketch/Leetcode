class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        for i in paths:
            if(i[1] not in [j[0] for j in paths]):
                return i[1]