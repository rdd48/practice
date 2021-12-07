class Solution:
    
    def isValid(self, s: str) -> bool:
        """
        https://leetcode.com/problems/valid-parentheses/
        This function checks whether a string contains valid parenthesis of (), [], and {}
        Concept: The string can only fail if:
            1. A closed parenthesis appears before an open counterpart.
            2. A closed parenthesis appears after a different shaped opening counterpart
            3. There are unparied open parentheses remaining. 

        Approach: loop through the string and keep a new string (p_str) of parentheses characters. 
        Append open parentheses to p_str. If we encounter a closed parentheses, check that the most
        recent paranthesis character was its open counterpart. If so, remove this open paren character
        from p_str.  If not, fail it. Finally, check at the end that all open parens are closed, i.e. len(p_str) == 0

        Runtime: 24 ms, faster than 96.19% of Python3 online submissions for Valid Parentheses.
        Memory Usage: 14.2 MB, less than 65.53% of Python3 online submissions for Valid Parentheses.
        """
        
        open_b = '([{'
        closed_b = '}])'
        
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        p_str = ''
        
        for ch in s:
            if ch in closed_b:
                if len(p_str) == 0:
                    return False
                elif p_str[-1] == d[ch]:
                    p_str = p_str[:-1]
                else:
                    return False
                
            if ch in open_b:
                p_str += ch
        
        if len(p_str) > 0:
            return False
        
        return True