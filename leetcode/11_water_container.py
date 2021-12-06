class Solution:
    def maxArea(self, height: List[int]) -> int:

        """
        problem link: https://leetcode.com/problems/container-with-most-water/
        given a list of heights, return the volume of the largest-volume rectangle that can be made
        
        to do this in o(n) time, it's critical to realize that the lowest height being used in the rectangle
        is contributing to its largest possible rectangle as is, so there's no need to check
        any other rectangle with that height. i.e., if height[0] == 1 and height[4] == 1, then the rectangle 
        between these points is larger than rectangles (0,3), (0, 2) or (0, 1), so reset the leftmost index to 1

        heavy inspiration for this solution came from user kitt's very helpful explanation here:
        https://leetcode.com/problems/container-with-most-water/discuss/6131/O(N)-7-line-Python-solution-72ms
        """
        
        l = 0
        r = len(height) - 1
        
        best = 0
        
        for i in range(len(height)):
            if r == l:
                return best
            if height[l] < height[r]:
                best = max(best, height[l] * (r-l))
                l += 1
            else:
                best = max(best, height[r] * (r-l))
                r -= 1
        
        return best