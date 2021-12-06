class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, i in enumerate(nums):
            diff = target - i
            if diff not in d:
                d[i] = idx
            else:
                return [idx, d[diff]]