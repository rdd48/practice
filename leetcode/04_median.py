class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combo = nums1 + nums2
        combo.sort()
        
        # arr is zero or one
        if len(combo) == 0:
            return []
        elif len(combo) == 1:
            return combo[0]
        
        mid = len(combo) // 2
        
        # arr is even
        if len(combo) % 2 == 0:
            return float(combo[mid-1] + combo[mid]) / 2.
        
        # arr is odd
        else:
            return float(combo[mid])