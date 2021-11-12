from longest_motif import longest_common_substr, process_fasta

names, fasta_dict = process_fasta('input/rosalind_kmp.txt')

def get_max_substr(sub_str, base_str):
    sub_str = sub_str[::-1]
    base_str = base_str[::-1]
    best_score = 0
    for i in range(1,len(sub_str)+1):
        if sub_str[0:i] == base_str[-i:]:
            best_score = i
    return(best_score)


def calc_failure_array(strng):
    failure_array = [0]
    for i in range(1, len(strng)):
        prev_val = failure_array[-1]
        if prev_val > 0:
            if strng[0:prev_val+1] == strng[i-prev_val:i+1]:
                failure_array.append(prev_val+1)
            else:
                max_substr = get_max_substr(strng[i-prev_val:i+1], strng[0:prev_val+1])
                failure_array.append(max_substr)

            # elif strng[0] == strng[i]:
            #     failure_array.append(1)
            # else:
            #     failure_array.append(0) 
        elif strng[0] == strng[i]:
            failure_array.append(1)
        else:
            failure_array.append(0)

    return ' '.join([str(i) for i in failure_array])

# print(calc_failure_array(fasta_dict[names[0]]))

with open('output/speed_up_motif_out.txt', 'w+') as output:
    output.write(calc_failure_array(fasta_dict[names[0]]))

