def searchPalindrome(low_i, high_i, s):
    while low_i >= 0 and high_i < len(s):
        if s[low_i] == s[high_i]:
            low_i -= 1
            high_i += 1
        else:
            break
        
    low_i += 1
    high_i -= 1

    return low_i, high_i

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

        # case when palindrome len is even
        low_i, high_i = searchPalindrome(i, i+1, s)

        curr_score = high_i - low_i
        if curr_score > best_score:
            best_score = curr_score
            best_low = low_i
            best_high = high_i
        
        # case when palindrome len is odd
        low_i, high_i = searchPalindrome(i-1, i+1, s)
       
        curr_score = high_i - low_i
        if curr_score > best_score:
            best_score = curr_score
            best_low = low_i
            best_high = high_i
    
    return s[best_low:best_high+1]

print(longestPalindrome('ccc'))
print(longestPalindrome('cccc'))
print(longestPalindrome('abc'))
print(longestPalindrome('dabccbae'))