class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Runtime: 28 ms, faster than 94.38% of Python3 online submissions for Longest Common Prefix.
        Memory Usage: 14.3 MB, less than 81.99% of Python3 online submissions for Longest Common Prefix.
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        min_len = len(min(strs, key=len))
        lcp = ''

        for i in range(1, min_len+1):
            curr = strs[0][:i]
            for s in strs[1:]:
                if s[:i] != curr:
                    return lcp
            lcp = curr

        return lcp
