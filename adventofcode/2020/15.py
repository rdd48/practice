with open('input/15.txt') as f:
    inp = f.readline().strip()
    nums = [int(i) for i in inp.split(',')]

    spoken = {i: idx+1 for idx, i in enumerate(nums[:-1])}
    prev = nums[-1]

    for rd in range(len(nums)+1, 30000000+1):
        if prev not in spoken:
            curr = 0
        else:
            curr = rd - 1 - spoken[prev]
        spoken[prev] = rd - 1
        prev = curr

        if rd == 2020:
            print('round one: ', curr)

    # naive bf for part two?
    # works fast enough lol. <1 min. not going to optiize
    print('round two: ', curr)