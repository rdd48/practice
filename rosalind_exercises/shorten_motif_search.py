from longest_motif import longest_common_substr, process_fasta

names, fasta_dict = process_fasta('input/test.txt')

def get_max_substr(substr, strng):
    substr = substr[::-1]
    strng = strng[::-1]
    max_len = 0
    print(substr, strng)
    for i in range(len(substr)):
        if strng[0] == substr[i]:
            temp_max_len = 1
            new_i = i + 1
            while new_i < len(substr):
                if strng[0:temp_max_len] == substr[i:new_i]:
                    new_i += 1
                    temp_max_len += 1
                else:
                    break
            if temp_max_len > max_len:
                max_len = temp_max_len 
    return(max_len)

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

print(calc_failure_array(fasta_dict[names[0]]))

