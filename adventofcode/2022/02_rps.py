# there's a smarter way to do this... will figure out tomorrow

throw_to_int = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

def tally_rps1(filename):
    total = 0
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            opp, play = l.strip().split()

            # score for what you threw
            total += throw_to_int[play]

            # score for if you tied:
            if throw_to_int[opp] == throw_to_int[play]:
                total += 3
            
            # opp throws rock
            elif throw_to_int[opp] == 1 and throw_to_int[play] == 2:
                total += 6
            
            # opp throws paper
            elif throw_to_int[opp] == 2 and throw_to_int[play] == 3:
                total += 6
            
            # opp throws scissors
            elif throw_to_int[opp] == 3 and throw_to_int[play] == 1:
                total += 6
    
    return total

# print(tally_rps('input/test.txt'))
print(tally_rps1('input/02.txt'))

def tally_rps2(filename):
    total = 0

    opp_choices = 'ABC'
    choice_to_points = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            opp, choice = l.strip().split()

            total += choice_to_points[choice] * 3

            if choice == 'Y':
                play = opp
            elif choice == 'X':
                play_idx = choice_to_points[opp] - 1
                play = opp_choices[play_idx]
            elif choice == 'Z':
                play_idx = (choice_to_points[opp] + 1) % 3
                play = opp_choices[play_idx]
            
            total += throw_to_int[play]

    
    return total

print(tally_rps2('input/test.txt'))
print(tally_rps2('input/02.txt'))