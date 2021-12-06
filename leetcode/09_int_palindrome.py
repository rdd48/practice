class Solution:
    def isPalindrome(self, x: int) -> bool:
        # solution where we convert to string:
        strx = str(x)
        rev_strx = strx[::-1]
        
        if strx == rev_strx:
            return True
        return False