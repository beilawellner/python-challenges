class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zero = {i:n for i, n in enumerate(nums)}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k in vec.non_zero:
            if k in self.non_zero:
                res += self.non_zero[k] * vec.non_zero[k]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)