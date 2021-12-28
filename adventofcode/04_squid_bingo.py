import numpy as np

class BingoBoard():
    def __init__(self, board_input):
        self.board = np.array(board_input)
        # self.board = self.board.astype('float')
    
    def print_board(self):
        print(self.board)

    def remove_pull(self, pull):
        x, y = np.where(self.board == pull)
        if x.size > 0 and y.size > 0:
            # this seems dumb but i'll have to think of something more clever
            self.board[x[0], y[0]] = np.nan
    
    def check_win(self):
        for i in range(5):
            # check rows
            if np.nansum(self.board[i,:]) == 0.:
                return True
            
            # check cols
            elif np.nansum(self.board[:,i]) == 0.:
                return True

        return False
    
    def sum_all_remaining_tiles(self):
        return np.nansum(self.board)
            

def process_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        pulls = lines[0].strip().split(',')

        lines = [l.strip() for l in lines if l.strip()]

        boards = []
        for idx in range(1, len(lines)-1, 5):
            str_board = [lst.split() for lst in lines[idx:idx+5]]
            float_board = [list(map(float, i)) for i in str_board]
            boards.append(BingoBoard(float_board))
        
        return pulls, boards

def i_win(filename):
    pulls, boards = process_input(filename)
    pulls = [float(p) for p in pulls]

    for p in pulls:
        for b in boards:
            b.remove_pull(p)
            if b.check_win():
                # b.print_board()
                return int(b.sum_all_remaining_tiles() * p)
        
def squid_wins(filename):
    pulls, boards = process_input(filename)
    pulls = [float(p) for p in pulls]

    boards_to_remove = []

    for p in pulls:
        for b in boards:
            b.remove_pull(p)
            if b.check_win():
                boards_to_remove.append(b)

        if boards_to_remove:
            for btr in boards_to_remove:
                boards.remove(btr)

                if len(boards) == 0:
                    # b.print_board()
                    return int(btr.sum_all_remaining_tiles() * p)

        boards_to_remove = []

print(i_win('input/4_bingo.txt'))
print(squid_wins('input/4_bingo.txt'))