# i'm not saying this is good or efficient code, but it do work

def get_new_paths(r, c, drc, rows, cols, streak):
    new_drcs = 'DRLU'
    new_paths = []
    for nd in new_drcs:
        if nd == 'D' and r < rows-1 and drc != 'U':
            new_streak = streak + 1 if nd == drc else 1
            if new_streak < 4:
                new_paths.append((r+1, c, 'D', new_streak))
        elif nd == 'U' and r > 0 and drc != 'D':
            new_streak = streak + 1 if nd == drc else 1
            if new_streak < 4:
                new_paths.append((r-1, c, 'U', new_streak))
        elif nd == 'R' and c < cols-1 and drc != 'L':
            new_streak = streak + 1 if nd == drc else 1
            if new_streak < 4:
                new_paths.append((r, c+1, 'R', new_streak))
        elif nd == 'L' and c > 0 and drc != 'R':
            new_streak = streak + 1 if nd == drc else 1
            if new_streak < 4:
                new_paths.append((r, c-1, 'L', new_streak))
    return new_paths

def check_shorter_streak(new_streak, new_score, new_r, new_c, best_scores, drc):
    for s in range(new_streak-1, 0, -1):
        if (new_r, new_c, drc, s) in best_scores:
            if best_scores[(new_r, new_c, drc, s)] <= new_score:
                return True
    return False

def main(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    grid = []
    for l in lines:
        grid.append([int(i) for i in l])

    rows, cols = len(grid), len(grid[0])

    best_scores = {
        (0,1,'R',1): grid[0][1],
        (1,0,'D',1): grid[1][0]
    }

    # paths is a set of r, c, score, dir, streak
    paths = [
        (0, 1, grid[0][1], 'R', 1), (1, 0, grid[1][0], 'D', 1)
    ]
    new_paths = paths.copy()
    
    while True:
        # print(len(paths))
        for r, c, score, drc, streak in paths:
            for new_r, new_c, new_drc, new_streak in get_new_paths(r, c, drc, rows, cols, streak):

                new_score = score + grid[new_r][new_c]
                if (new_r, new_c, new_drc, new_streak) not in best_scores:
                    # only add to best_scores if there isn't a shorter streak w smaller score
                    if not check_shorter_streak(new_streak, new_score, new_r, new_c, best_scores, new_drc):
                        best_scores[(new_r, new_c, new_drc, new_streak)] = new_score

                        new_paths.append((new_r, new_c, new_score, new_drc, new_streak))
                else:
                    if new_score < best_scores[(new_r, new_c, new_drc, new_streak)]:
                        best_scores[(new_r, new_c, new_drc, new_streak)] = new_score

                        new_paths.append((new_r, new_c, new_score, new_drc, new_streak))

            # if r == rows-1 and c == cols-1:
            #     print(score, curr_path)
        if not len(new_paths):
            break

        paths = new_paths.copy()
        new_paths = []
    ans = 99999999999
    for drc in 'UDRL':
        for k,score in best_scores.items():
            if k[0] == rows-1 and k[1] == cols-1:
                ans = min(ans, score)
    return ans

def get_new_paths2(r, c, drc, rows, cols, streak):
    if streak < 4:
        new_drcs = drc
    elif streak > 9:
        new_drcs = 'DRLU'.replace(drc, '')
    else:
        new_drcs = 'DRLU'
    new_paths = []
    for nd in new_drcs:
        if nd == 'D' and r < rows-1 and drc != 'U':
            new_streak = streak + 1 if nd == drc else 1
            new_paths.append((r+1, c, 'D', new_streak))
        elif nd == 'U' and r > 0 and drc != 'D':
            new_streak = streak + 1 if nd == drc else 1
            new_paths.append((r-1, c, 'U', new_streak))
        elif nd == 'R' and c < cols-1 and drc != 'L':
            new_streak = streak + 1 if nd == drc else 1
            new_paths.append((r, c+1, 'R', new_streak))
        elif nd == 'L' and c > 0 and drc != 'R':
            new_streak = streak + 1 if nd == drc else 1
            new_paths.append((r, c-1, 'L', new_streak))
    return new_paths

def main2(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    grid = []
    for l in lines:
        grid.append([int(i) for i in l])

    rows, cols = len(grid), len(grid[0])

    best_scores = {
        (0,1,'R',1): grid[0][1],
        (1,0,'D',1): grid[1][0]
    }

    # paths is a set of r, c, score, dir, streak
    paths = [
        (0, 1, grid[0][1], 'R', 1), (1, 0, grid[1][0], 'D', 1)
    ]
    new_paths = paths.copy()
    
    while True:
        print(len(paths))
        for r, c, score, drc, streak in paths:
            for new_r, new_c, new_drc, new_streak in get_new_paths2(r, c, drc, rows, cols, streak):

                new_score = score + grid[new_r][new_c]
                if (new_r, new_c, new_drc, new_streak) not in best_scores:
                    # only add to best_scores if there isn't a shorter streak w smaller score
                    #if not check_shorter_streak(new_streak, new_score, new_r, new_c, best_scores, new_drc):
                    best_scores[(new_r, new_c, new_drc, new_streak)] = new_score
                    new_paths.append((new_r, new_c, new_score, new_drc, new_streak))
                else:
                    if new_score < best_scores[(new_r, new_c, new_drc, new_streak)]:
                        best_scores[(new_r, new_c, new_drc, new_streak)] = new_score
                        new_paths.append((new_r, new_c, new_score, new_drc, new_streak))


        if not len(new_paths):
            break

        paths = new_paths.copy()
        new_paths = []
    ans = 99999999999
    for drc in 'UDRL':
        for k,score in best_scores.items():
            if k[0] == rows-1 and k[1] == cols-1 and k[-1] >= 4:
                ans = min(ans, score)
    return ans
    
    
print(main('input/17.txt'))
print(main2('input/17.txt'))