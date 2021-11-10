# from longest_motif import process_fasta

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def main(num_str):
    # prob of AaBb offspring always 25% if one parent is AaBb
    nums = num_str.split(' ')
    k = int(nums[0]) # generation number
    n = int(nums[1]) # num childred to calc probability on
    pop = 2 ** k

    # calc probability from binomial distr:
    # http://saradoesbioinformatics.blogspot.com/2016/07/independent-alleles.html
    # in words:
    # sum from n to population total (2**k):
    # num combinations * (0.25 ** current_val) * (0.75 ** (pop - current_val))

    probability = 0
    for i in range(n, pop + 1):
        combos = factorial(pop) / (factorial(i) * factorial(pop-i))
        probability += combos * (0.25 ** i) * (0.75 **(pop-i))
    return(probability)



print(main('5 9'))