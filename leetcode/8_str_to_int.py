class Solution:

    def check_in_range(val, neg_value=False):
            if neg_value:
                mod = -1
            else:
                mod = 1

            if mod * int(val) < -2**31:
                return -2147483648
            elif mod * int(val) > (2**31) - 1:
                return 2147483647
            else:
                return mod * int(val)
        
    def myAtoi(self, s: str) -> int:

        # remove leading spaces
        s = s.strip()

        # return 0 for empty strings or '-' only case
        if not s or s == '-':
            return 0

        nums = '0123456789'

        if s[0] == '-':
            if s[1] not in nums:
                return 0

            s_new = ''
            for i in s[1:]:
                if i in nums:
                    s_new += i
                else:
                    return self.check_in_range(s_new, neg_value=True)

            return self.check_in_range(s_new, neg_value=True)      
            
        elif s[0] not in nums and s[0] != '+':
            return 0
        else:
            if s[0] == '+':
                if len(s) == 1:
                    return 0
                s = s[1:]
            s_new = ''
            for i in s:
                if i in nums:
                    s_new += i
                else:
                    if not s_new:
                        return 0
                    return self.check_in_range(s_new, neg_value=False)
                    
            return self.check_in_range(s_new, neg_value=False)