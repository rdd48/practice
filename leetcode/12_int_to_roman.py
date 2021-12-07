def getRomanVal(val, pos):
    """this function takes in a value and the base 10 pos, i.e. 1s, 10s, 100s.
    This returns the letters corresponding to that base 10 position """
    if val == 0:
        return ''

    if pos == 1:
        letters = 'IVX'
    elif pos == 10:
        letters = 'XLC'
    elif pos == 100:
        letters = 'CDM'

    if val == 4:
        return letters[:2]
    elif val == 9:
        return letters[0] + letters[2]

    else:
        if val > 0 and val < 5:
            return ''.join([letters[0] for _ in range(val % 5)])
        elif val >= 5:
            return letters[1] + ''.join([letters[0] for _ in range(val % 5)])

def intToRoman(num: int) -> str:

    """Runtime: 36 ms, faster than 98.66% of Python3 online submissions for Integer to Roman.
    Memory Usage: 14.5 MB, less than 28.68% of Python3 online submissions for Integer to Roman."""
        
    if num == 0:
        return 0

    ones_val = num % 10
    ans = getRomanVal(ones_val, 1)

    if num < 10:
        return ans

    tens_val = (num // 10) % 10
    ans = getRomanVal(tens_val, 10) + ans
        
    if num < 100:
        return ans

    huns_val = (num // 100) % 10
    ans = getRomanVal(huns_val, 100) + ans
        
    if num < 1000:
        return ans

    thou_val = (num // 1000) % 10
    ans = ''.join(['M' for _ in range(thou_val % 5)]) + ans

    return ans

print(intToRoman(10))
print(intToRoman(60))
print(intToRoman(69))
print(intToRoman(1992))