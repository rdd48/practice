import pygame
import random

pygame.init()

# global varaibles for window
width, height = 800, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minesweeper")

# global variables for boxes
side_bumper = 10
cols = 30
rows = 16
num_boxes = rows * cols
box_width = (width - (2 * side_bumper)) / cols
box_height = (height - (2 * side_bumper)) / rows

# global variables for click events
clicked_boxes = []
clicked_mines = []
clicked_flags = []

def get_box_from_click(m_x, m_y):
    # return False if click is outside boxes
    if (m_x < side_bumper) or (m_x > width - side_bumper)\
        or (m_y < side_bumper) or (m_y > height - side_bumper):
        return 'border'

    box_row = (m_y - side_bumper) // box_height
    box_col = (m_x - side_bumper) // box_width

    # convert to the number of the box used when drawing the window
    box_num = int(box_col) + (int(box_row) * cols)

    return box_num

def get_xy_from_box(box_num):

    box_xpos = (side_bumper + ((box_num % cols) * box_width)) + 4
    box_ypos = (side_bumper+ ((box_num // cols) * box_height)) + 1


    return box_xpos, box_ypos

def draw_char_on_win(box_num, char):

    # pygame.draw.circle(win, (0, 0, 0), (x,y), radius, 3)
    letter_font = pygame.font.SysFont('Helvetica', 30)
    text = letter_font.render(char, 1, (0,0,0))
    box_xpos, box_ypos = get_xy_from_box(box_num)

    win.blit(text, (box_xpos, box_ypos))

    # pygame.display.update()

def is_edge(box_num):
    # using compass directions for clarity, so top is north, right is east, etc.
    # first, determine if we are on the top or bottom row
    top_row, bottom_row, left_col, right_col = False, False, False, False
    if box_num < cols:
        top_row = True
    if box_num >= (cols * rows) - cols:
        bottom_row = True
    if box_num % cols == 0:
        left_col = True
    if box_num % cols == cols - 1:
        right_col = True

    return top_row, bottom_row, left_col, right_col

def get_mine_number(box_num):
    # using compass directions for clarity, so top is north, right is east, etc.
    # first, determine if we are on the top or bottom row

    top_row, bottom_row, left_col, right_col = is_edge(box_num)
    
    # initiate neighbor positions
    nbr_pos = []

    # north & south neighbor:
    if not top_row:
        n_nbr = box_num - cols
        nbr_pos.append(n_nbr)
        if not left_col:
            nw_nbr = box_num - cols - 1
            nbr_pos.append(nw_nbr)
        if not right_col:
            ne_nbr = box_num - cols + 1
            nbr_pos.append(ne_nbr)

    if not bottom_row:
        s_nbr = box_num + cols
        nbr_pos.append(s_nbr)
        if not left_col: 
            sw_nbr = box_num + cols - 1
            nbr_pos.append(sw_nbr)
        if not right_col:
            se_nbr = box_num + cols + 1
            nbr_pos.append(se_nbr)

    # right & left neighbors:
    if not left_col:
        w_nbr = box_num - 1
        nbr_pos.append(w_nbr)
    if not right_col:
        e_nbr = box_num + 1
        nbr_pos.append(e_nbr)
    
    mines = 0
    for n in nbr_pos:
        if n in mine_locations:
            mines += 1
    
    return mines

def generate_opening_zeros(box_num):
    num_starting_zeros = random.randint(10, 25)

    # initialize with first box clicked (aka box_num)
    opening_zeros = [box_num]

    # all 8 surrounding boxes can't have any mines either:
    top_row, bottom_row, left_col, right_col = is_edge(box_num)
    if not top_row:
        opening_zeros.append(box_num - cols)
        if not left_col:
            opening_zeros.append(box_num - cols - 1)
        if not right_col:
            opening_zeros.append(box_num - cols + 1)
    if not bottom_row:
        opening_zeros.append(box_num + cols)
        if not left_col:
            opening_zeros.append(box_num + cols - 1)
        if not right_col:
            opening_zeros.append(box_num + cols + 1)
    if not left_col:
        opening_zeros.append(box_num - 1)
    if not right_col:
        opening_zeros.append(box_num + 1)

    # walk randomly around for number in num_starting_zeros, skipping the first one
    for i in range(num_starting_zeros - 1):
        edge_list = ([top_row, bottom_row, left_col, right_col])
        not_edges = [i for i, bool in enumerate(edge_list) if not bool]
        
        random_val = random.choice(not_edges)

        if random_val == 0:
            box_num -= cols
            opening_zeros.append(box_num)
        elif random_val == 1:
            box_num += cols
            opening_zeros.append(box_num)
        elif random_val == 2:
            box_num -= 1
            opening_zeros.append(box_num)
        elif random_val == 3:
            box_num += 1
            opening_zeros.append(box_num)
    
    return opening_zeros

def generate_opening_mines(box_num, num_mines):
    opening_zeros = generate_opening_zeros(box_num)
    mines = []
    mine_nums = list(range(num_mines))
    box_nums = set(range(num_boxes))
    for i in mine_nums:
        choices = list(box_nums - set(mines) - set(opening_zeros))
        mines.append(random.choice(choices))
    
    # print(opening_zeros, mines)
    return mines



def get_neighbor_zeros_recur(box_num, zeros=None, visited=None):

    if not zeros:
        zeros = []
        visited = []

    top_row, bottom_row, left_col, right_col = is_edge(box_num)


    if not top_row:
        # check if north box is zero & add to list
        n_box = box_num - cols
        n_mines = get_mine_number(n_box)
        if n_box not in visited:
            visited.append(n_box)
            zeros.append([n_box, n_mines])
            if n_mines == 0:
                get_neighbor_zeros_recur(n_box, zeros, visited)
        if not left_col:
            nw_box = n_box - 1
            nw_mines = get_mine_number(nw_box)
            # check if left box is zero
            if nw_box not in visited:
                visited.append(nw_box)
                zeros.append([nw_box, nw_mines])
                if nw_mines == 0:
                    get_neighbor_zeros_recur(nw_box, zeros, visited)
        if not right_col:
            ne_box = n_box + 1
            ne_mines = get_mine_number(ne_box)
            # check if left box is zero
            if ne_box not in visited:
                visited.append(ne_box)
                zeros.append([ne_box, ne_mines])
                if ne_mines == 0:
                    get_neighbor_zeros_recur(ne_box, zeros, visited)
                

    if not bottom_row:
        s_box = box_num + cols
        s_mines = get_mine_number(s_box)
        # check if south box is zero
        if s_box not in visited: 
            visited.append(s_box)
            zeros.append([s_box, s_mines])
            if s_mines == 0:
                get_neighbor_zeros_recur(s_box, zeros, visited)
        if not left_col:
            sw_box = s_box - 1
            sw_mines = get_mine_number(sw_box)
            # check if left box is zero
            if sw_box not in visited:
                visited.append(sw_box)
                zeros.append([sw_box, sw_mines])
                if sw_mines == 0:
                    get_neighbor_zeros_recur(sw_box, zeros, visited)
        if not right_col:
            se_box = s_box + 1
            se_mines = get_mine_number(se_box)
            # check if left box is zero
            if se_box not in visited:
                visited.append(se_box)
                zeros.append([se_box, se_mines])
                if se_mines == 0:
                    get_neighbor_zeros_recur(se_box, zeros, visited)

    if not left_col:
        w_box = box_num - 1
        w_mines = get_mine_number(w_box)
        # check if left box is zero
        if w_box not in visited:
            visited.append(w_box)
            zeros.append([w_box, w_mines])
            if w_mines == 0:
                get_neighbor_zeros_recur(w_box, zeros, visited)
    if not right_col:
        e_box = box_num + 1
        e_mines = get_mine_number(e_box)
        # check if left box is zero
        if e_box not in visited:
            visited.append(e_box)
            zeros.append([e_box, e_mines])
            if e_mines == 0:
                get_neighbor_zeros_recur(e_box, zeros, visited)

    return(zeros)

def draw_window():
    
    win.fill((255, 255, 255)) # RGB color in tuple
    
    # create outer box first
    # Rect object: Rect(left, top, width, height)
    button_box = pygame.Rect(side_bumper, side_bumper, width - (2 * side_bumper), height - (2 * side_bumper))
    pygame.draw.rect(win, (0,0,0), button_box, width=3)


    for i in range(num_boxes):
        box_xpos = side_bumper + ((i % cols) * box_width)
        box_ypos = side_bumper + ((i // cols) * box_height)

        if i in clicked_boxes:
            button_box = pygame.Rect(box_xpos, box_ypos, box_width, box_height)
            pygame.draw.rect(win, (100,100,100), button_box)

            button_border = pygame.Rect(box_xpos, box_ypos, box_width, box_height)
            pygame.draw.rect(win, (0,0,0), button_border, width=1)

        else:
            button_border = pygame.Rect(box_xpos, box_ypos, box_width, box_height)
            pygame.draw.rect(win, (0,0,0), button_border, width=1)
    
    for i, num_mines in clicked_boxes:
        draw_char_on_win(i, chr(48 + num_mines))
    
    for i in clicked_mines:
        draw_char_on_win(i, chr(88))
    
    for i in clicked_flags:
        draw_char_on_win(i, chr(63))


    # display_font = pygame.font.SysFont('comicsans', 25)
    # header_text = display_font.render("Player 2: Guess the word!", 1, (0,0,0))
    # win.blit(header_text, (50, 50))
    # submit_text = letter_font.render('SUBMIT', 1, (0,0,0))
    # win.blit(submit_text, (625, 260))

    pygame.display.update()


def main(): 
    fps = 60
    clock = pygame.time.Clock()
    run = True

    # start game with randomly-generated mine locations
    num_mines = 100
    global mine_locations
    mine_locations = []

    while run:
        clock.tick(fps)
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            button_mods = pygame.key.get_mods()
            if event.type == pygame.MOUSEBUTTONDOWN and not button_mods:
                m_x, m_y = pygame.mouse.get_pos()
                box_num = get_box_from_click(m_x, m_y)

                # check if click within boxes
                if box_num != 'border':

                    if not mine_locations:
                        # global mine_locations
                        mine_locations = generate_opening_mines(box_num, num_mines)

                    if box_num in mine_locations:
                        clicked_mines.append(box_num)
                        
                    else:
                        num_mines = get_mine_number(box_num)
                        clicked_boxes.append([box_num, num_mines])
                        if get_mine_number(box_num) == 0:
                            zeros = get_neighbor_zeros_recur(box_num)
                            if zeros:
                                for z, num_mines in zeros:
                                    clicked_boxes.append([z, num_mines])
                    
                    if box_num in clicked_flags:
                        clicked_flags.remove(box_num)
                    
            elif event.type == pygame.MOUSEBUTTONDOWN and button_mods in [64, 8256]: # ctrl click w/o and w/ caps lock
                m_x, m_y = pygame.mouse.get_pos()
                box_num = get_box_from_click(m_x, m_y)

                # check if click within boxes
                if box_num != 'border':
                    clicked_flags.append(box_num)



if __name__ == '__main__':

    status = True
    while status:
        status = main()

pygame.quit()