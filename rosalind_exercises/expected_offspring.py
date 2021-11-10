# from longest_motif import process_fasta

def main(num_str):
    nums = num_str.split(' ')
    expected = 0
    for i in range(len(nums)):
        if i <= 2:
            expected += 2 * int(nums[i])
        elif i == 3:
            expected += 1.5 * int(nums[i])
        elif i == 4:
            expected += 1.0 * int(nums[i])
    
    return expected



print(main('16253 16496 17932 17831 17244 16110'))