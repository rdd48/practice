class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # faster solution pulled from forums
        
        start, maxlen, d = 0, 0, {}
        
        for i, ch in enumerate(s):
            if ch in d and start <= d[ch]:
                start = d[ch] + 1
            else:
                maxlen = max(maxlen, i - start + 1)
            d[ch] = i
        
        return maxlen
        
        # naive solution i first came up with
        
        count = 0
        best_count = 0
        running_str = ''
        for i in range(len(s)):
            if s[i] not in running_str:
                count += 1
                running_str += s[i]
            elif s[i] in running_str:
                if count > best_count:
                    best_count = count
                
                running_str = s[i]
                running_i = i-1
                
                while running_i >= 0 and s[running_i] not in running_str:
                    running_str += s[running_i]
                    running_i -= 1
                
                count = len(running_str)
            
        if count > best_count:
            return count
        return best_count
            
                
            