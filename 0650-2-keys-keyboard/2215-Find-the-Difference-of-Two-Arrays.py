class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        for num in set2.copy():
            if num in set1:
                set1.remove(num)
                set2.remove(num)
        return [list(set1), list(set2)]