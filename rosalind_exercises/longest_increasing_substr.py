with open('input/rosalind_lgis.txt') as f:
    lines = f.readlines()
    arr = lines[1].split(' ')
    arr = [int(i) for i in arr]
 
def lis(arr):
    '''Function to determine the longest increasing subsequence (LIS). 
    Input is a list of ints. Output is a the LIS as a list of ints'''

    # LIS means longest increasing sequence here, not list
    LIS = [None] * len(arr)

    # this will be where we store the best LIS as we go through the list
    LIS[0] = [arr[0]]

    for i in range(1, len(arr)):

        # this iterator lets us check against all previous best LIS scores
        for j in range(i):

            # case when our value is lower than the highest value of a previous best LIS
            # e.g., say the best solution at length 2 was [0, 10] and our new arr[i] is 5
            # so we replace the best len 2 solution with [0, 5]
            if arr[i] < LIS[j][-1]:
                if j == 0:
                    sub_arr = LIS[j].copy()
                    sub_arr[-1] = arr[i]
                    LIS[j] = sub_arr
                    break

                # this checks for cases where our current value is larger than the preceeding value
                # e.g., if our value is 6, our list at len 1 was [3], and our list at 2 is [5, 10], we want 2 to be [5, 6]
                elif arr[i] > LIS[j][-2]:
                    sub_arr = LIS[j].copy()
                    sub_arr[-1] = arr[i]
                    LIS[j] = sub_arr
                    break

                # but here, if our value at list 2 was [9, 10], we want len 2 to be [3, 6] instead of [9, 6]
                else:
                    sub_arr = LIS[j-1].copy()
                    sub_arr.append(arr[i])
                    LIS[j] = sub_arr
                    break

            # case when our value is higher than all highest values
            # so we store a new LIS at the next position and append our val
            # e.g., the longest prev solution was [0, 5] and our val is 10
            # so at idx 3 in LIS we store [0, 5, 10]
            elif arr[i] > LIS[j][-1] and LIS[j+1] is None:
                sub_arr = LIS[j].copy()
                sub_arr.append(arr[i])
                LIS[j+1] = sub_arr
                break
    
    # our solution is now the longest list in LIS
    # since the list_len always stored at that index - 1, return that index
    list_len = [len(i) if i is not None else 0 for i in LIS]
    max_len = max(list_len)
    return LIS[max_len - 1]

def lds(arr):
    '''Function to determine the longest decreasing subsequence (LDS). 
    Input is a list of ints. Output is a the LDS as a list of ints'''

    LDS = [None] * len(arr)
    LDS[0] = [arr[0]]

    for i in range(1, len(arr)):

        for j in range(i):

            if arr[i] > LDS[j][-1]:
                if j == 0:
                    LDS[j] = [arr[i]]
                    break
                else:
                    sub_arr = LDS[j-1].copy()
                    sub_arr.append(arr[i])
                    LDS[j] = sub_arr
                    break
            elif arr[i] < LDS[j][-1] and LDS[j+1] is None:
                sub_arr = LDS[j].copy()
                sub_arr.append(arr[i])
                LDS[j+1] = sub_arr
                break
        
    
    list_len = [len(i) if i is not None else 0 for i in LDS]
    max_len = max(list_len)
    return LDS[max_len - 1]

if __name__ == '__main__':

    print(' '.join([str(i) for i in lis(arr)]))
    print(' '.join([str(i) for i in lds(arr)]))
