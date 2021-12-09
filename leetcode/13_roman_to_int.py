class Solution:
    def romanToInt(self, s: str) -> int:

        """
        Runtime: 44 ms, faster than 84.88% of Python3 online submissions for Roman to Integer.
        Memory Usage: 14.2 MB, less than 84.56% of Python3 online submissions for Roman to Integer.
        """
        
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        val = 0
        prev_ch = 1 # will be used for deleting vals
        
        # loop through backwards
        for ch in s[::-1]:
            if d[ch] < prev_ch:
                val -= d[ch]
            else:
                val += d[ch]
            
            prev_ch = d[ch]
        
        return val