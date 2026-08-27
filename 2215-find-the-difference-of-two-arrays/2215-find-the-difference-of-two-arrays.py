class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr=[]
        for i in range(1):
            arr1=[]
            for j in nums1:
                if(j not in nums2 and j not in arr1):
                    arr1.append(j)
            arr2=[]
            for k in nums2:
                if(k not in nums1 and k not in arr2):
                    arr2.append(k)
            arr.append(arr1)
            arr.append(arr2)
        return arr