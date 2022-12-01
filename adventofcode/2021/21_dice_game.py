def roll_dice(dice_pos):
    moves = 0
    for _ in range(3):
        if dice_pos < 100:
            dice_pos += 1
        elif dice_pos == 100:
            dice_pos = 1
        moves += dice_pos
    return moves, dice_pos


def get_board_pos(roll, curr_pos):
    new_pos = (roll + curr_pos) % 10
    return new_pos if new_pos > 0 else 10


def reverse_turn(p1_turn):
    return (False, True) if p1_turn else (True, False)


def main_1(pos1, pos2):
    # no input needed to process today besides two starting positions
    score1, score2 = 0, 0
    p1_turn, p2_turn = True, False

    dice_pos = 0
    rolls = 0

    while score1 < 1000 and score2 < 1000:
        rolls += 3
        if p1_turn:
            moves, dice_pos = roll_dice(dice_pos)
            pos1 = get_board_pos(moves, pos1)
            score1 += pos1

            # print(f'Roll {rolls}: P1 space {pos1} score {score1}')

        elif p2_turn:
            moves, dice_pos = roll_dice(dice_pos)
            pos2 = get_board_pos(moves, pos2)
            score2 += pos2

            # print(f'Roll {rolls}: P2 space {pos2} score {score2}')

        p1_turn, p2_turn = reverse_turn(p1_turn)

    if p2_turn:
        # ie, we won on player one's turn
        return score2 * rolls

    # ie, we won on player 2's turn
    return score1 * rolls


def main_2(pos1, pos2):

    d = {}

    # keys = (player1_pos, player2_pos, player1_score, player2_score)
    # values = num games at this stage?
    d[(pos1, pos2, 0, 0)] = 1

    p1_turn, p2_turn = True, False
    turns = 0

    p1_wins = 0
    p2_wins = 0

    # i.e., each turn 27 new games are created with these combined rolls
    rolls = []
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            for k in (1, 2, 3):
                rolls.append(i+j+k)

    while True:
        turns += 1
        d_copy = {}
        for k, v in d.items():
            pos1, pos2, score1, score2 = k
            num_games = v
            for roll in rolls:
                if p1_turn:
                    new_pos = get_board_pos(roll, pos1)

                    if score1 + new_pos >= 21:
                        p1_wins += v

                    elif (new_pos, pos2, score1 + new_pos, score2) not in d_copy.keys():
                        d_copy[(new_pos, pos2, score1 +
                                new_pos, score2)] = num_games
                    else:
                        d_copy[(new_pos, pos2, score1 +
                                new_pos, score2)] += num_games
                elif p2_turn:
                    new_pos = get_board_pos(roll, pos2)
                    if score2 + new_pos >= 21:
                        p2_wins += v

                    elif (pos1, new_pos, score1, score2 + new_pos) not in d_copy.keys():
                        d_copy[(pos1, new_pos, score1,
                                score2 + new_pos)] = num_games
                    else:
                        d_copy[(pos1, new_pos, score1,
                                score2 + new_pos)] += num_games
            d = d_copy
        p1_turn, p2_turn = reverse_turn(p1_turn)

        # print(turns, len(d))
        if len(d) == 0:
            return max(p1_wins, p2_wins)


# print(main_1(4, 8))
print(main_1(4, 6))

# print(main_2(4, 8))
print(main_2(4, 6))
