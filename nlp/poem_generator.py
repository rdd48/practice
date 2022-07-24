import numpy as np

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def remove_punc(l):
    split_l = l.split()
    new_l = []
    for word in split_l:
        no_punc = ''
        for char in word:
            if char not in punc:
                no_punc += char
        if no_punc:
            new_l.append(no_punc.lower())
    return new_l

def poem_to_words(txt_file):
    '''train test split + split lines from input'''
    saved_words = []
    with open(txt_file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            # check that line has data
            if len(l.strip()) > 0:
                # split and remove punctuation
                split_l = remove_punc(l)
                for word in split_l:
                    saved_words.append(word)
    return saved_words

def poem_to_list(txt_file):
    '''train test split + split lines from input'''
    saved_lines = []
    with open(txt_file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            # check that line has data
            if len(l.strip()) > 0:
                # split and remove punctuation
                split_l = remove_punc(l)
                saved_lines.append(split_l)
    return saved_lines

frost_list = poem_to_list('input/robert_frost.txt')

# don't judge. i realized late that i needed int2word and word2int, so this was quicker than thinking
word2int = {}
idx = 0
for line in frost_list:
    for word in line:
        if word not in word2int:
            word2int[word] = idx
            idx += 1

int2word = {v: k for k, v in word2int.items()}

pi, A1, A2 = {}, {}, {}

for line in frost_list:
    for idx, word in enumerate(line):
        if idx == 0:
            if word == 'trodden':
                print('wtf?')
            # store word in pi
            if word not in pi:
                pi[word2int[word]] = 0
            pi[word2int[word]] += 1.
        if idx < len(line) - 1:
            # store word in A1
            if word2int[word] not in A1:
                A1[word2int[word]] = {}
            word_plus1 = line[idx+1]
            if word_plus1 not in A1[word2int[word]]:
                A1[word2int[word]][word2int[word_plus1]] = 0
            A1[word2int[word]][word2int[word_plus1]] += 1.
        if idx < len(line) - 2:
            # store word in A2:
            if word2int[word] not in A2:
                A2[word2int[word]] = {}
            if word2int[word_plus1] not in A2[word2int[word]]:
                A2[word2int[word]][word2int[word_plus1]] = {}
            word_plus2 = line[idx+2]
            if word2int[word_plus2] not in A2[word2int[word]][word2int[word_plus1]]:
                A2[word2int[word]][word2int[word_plus1]][word2int[word_plus2]] = 0
            A2[word2int[word]][word2int[word_plus1]][word2int[word_plus2]] += 1.

def norm_dict_values(d):
    if len(d) == 1:
        for k in d.keys():
            return {k: 1.}
    cum_sum = sum(d.values())
    probs = {}
    for k,v in d.items():
        probs[k] = v / cum_sum
    
    return probs

A2_norm = {}
A1_norm = {}

for k1 in A2:
    if k1 not in A2_norm:
        A2_norm[k1] = {}
    for k2 in A2[k1]:
        A2_norm[k1][k2] = norm_dict_values(A2[k1][k2])

for k1 in A1:
    A1_norm[k1] = norm_dict_values(A1[k1])

pi_norm = norm_dict_values(pi)

# time to generate
# get first word from pi_norm dist
# get second word from A1_norm[word - 1] dist
# get rest of line from A2_norm[word - 2][word - 1] dist

# test with a 10 word sentence

def generate_sentence(max_len):
    for idx in range(max_len):
        if idx == 0:
            first_word = np.random.choice(list(pi_norm.keys()), p=list(pi_norm.values()))
            int_sentence = [first_word]
            word_sentence = int2word[first_word]
        elif idx == 1:
            second_word = np.random.choice(list(A1_norm[first_word].keys()), p=list(A1_norm[first_word].values()))
            int_sentence.append(second_word)
            word_sentence += f' {int2word[second_word]}'
        else:
            word_minus2 = int_sentence[idx-2]
            word_minus1 = int_sentence[idx-1]

            if word_minus2 not in A2_norm:
                return f'{word_sentence}.'
                # word_sentence += '.'
            if word_minus1 not in A2_norm[word_minus2]:
                return f'{word_sentence}.'
                    
            else:
                choices = list(A2_norm[word_minus2][word_minus1].keys())
                probs = list(A2_norm[word_minus2][word_minus1].values())
                following_word = np.random.choice(choices, p=probs)
                
                int_sentence.append(following_word)
                word_sentence += f' {int2word[following_word]}'

    return word_sentence

for _ in range(4):
    print(generate_sentence(max_len=10))
