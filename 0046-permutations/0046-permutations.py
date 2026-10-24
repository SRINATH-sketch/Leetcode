from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        arr=[]
        for i in permutations(nums):
            arr.append(i)
        return arr