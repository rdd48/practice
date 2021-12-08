def isMatch(s: str, p: str) -> bool:

    """
    Brute force method. still WIP, doesn't work for all cases yet
    """

    if not s:
        return False #?
    if p == '.*':
        return True

    star_val = ''
    p_idx = 0
    for idx, ch in enumerate(s):
        if ch == p[p_idx] or ch == '.':
            p_idx += 1
            if p_idx == len(p):
                if idx == len(s) - 1:
                    return True
                else:
                    return False

        elif p[p_idx] == '*':
            if not star_val:
                star_val = s[idx-1]
            if ch != star_val:
                star_val = ''
                p_idx += 1
                if p_idx < len(p):
                    if p[p_idx] == '.':
                        return True
                    if p[p_idx] == ch:
                        p_idx += 1
                    else:
                        return False

        elif ch != p[p_idx]:

            # only saving case if it's a character followed by
            # a star followed by the rest, so jump ahead 2

            if p_idx < len(p) - 1:
                if p[p_idx+2] == ch or p[p_idx+2] == '.':
                    p_idx += 2
            else:
                return False

    return True

print(isMatch('aa', 'aa'))