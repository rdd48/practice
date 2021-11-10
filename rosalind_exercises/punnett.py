def offspring_from_parents(p1, p2):
    pass

def predict_offspring(k, m, n):
    # maiting options -> outcomes:
    # 1 AA + 1 AA => 1 AA 
    # 1 AA + 1 aa => 1 Aa
    # 1 aa + 1aa => 1 aa

    # so the probability of having the trait equals:
    # 1 - prob first allele is rec - prob second allele is rec

    total = k+m+n
    
    # second neg: prob 
    second_neg = ((m/total) * ((m-1)/(total-1))) * 0.25
    second_neg += (m/total) * (n/(total-1)) * (0.5)
    second_neg += (n/total) * (m/(total-1)) * 0.5
    second_neg += (n/total) * ((n-1)/(total-1))

    return(1 - second_neg)

print(predict_offspring(30, 27, 26))