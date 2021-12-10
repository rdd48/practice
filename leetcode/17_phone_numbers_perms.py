def letterCombinations(digits: str):
    d = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    if len(digits) == 0:
        return ''

    final = ['']
    for i in digits:
        curr = []
        for ch in d[i]:
            for perm in final:
                curr.append(perm + ch)
        
        final = curr
    
    return final

print(letterCombinations('234'))