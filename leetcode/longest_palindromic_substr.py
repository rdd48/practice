def longestPalindrome(s: str) -> str:

    if len(s) == 1:
        return s
    elif len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    
    best_score = 0
    best_low, best_high = 0, 0

    for i, ch in enumerate(s):
        low_i = i
        high_i = i + 1

        # adjust high_i for case where palindrome len is even
        while low_i >= 0 and high_i < len(s):
            if s[low_i] == s[high_i]:
                low_i -= 1
                high_i += 1
            else:
                break
        
        low_i += 1
        high_i -= 1

        curr_score = high_i - low_i
        if curr_score > best_score:
            best_score = curr_score
            best_low = low_i
            best_high = high_i

        low_i = i - 1
        high_i = i + 1

        while low_i >= 0 and high_i < len(s):
            if s[low_i] == s[high_i]:
                low_i -= 1
                high_i += 1
            else:
                break
        
        # readjust the i's
        low_i += 1
        high_i -= 1

        curr_score = high_i - low_i
        if curr_score > best_score:
            best_score = curr_score
            best_low = low_i
            best_high = high_i
    
    return s[best_low:best_high+1]

print(longestPalindrome('cc'))