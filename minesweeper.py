import pygame
import random

pygame.init()

# global varaibles for window
width, height = 800, 550
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minesweeper")

# global variables for boxes
header = 50
side_bumper = 10
cols = 30
rows = 16
num_boxes = rows * cols
box_width = (width - (2 * side_bumper)) / cols
box_height = (height - header - (2 * side_bumper)) / rows

# grey colors for background and tiles
greys = (130, 180, 230)

# red colors for mine numbers
reds = [i for i in range(10, 231, 30)]
reds = reds[::-1]

# global variables for click events
clicked_boxes = []
clicked_flags = []
display_mines = False
click_and_held_box = -1 # can't be False, because of box 0, but basically False

def get_box_from_click(m_x, m_y):
    # return border str if click is outside boxes
    if (m_x < side_bumper) or (m_x > width - side_bumper)\
        or (m_y < side_bumper + header) or (m_y > height - side_bumper):
        return 'border'

    box_row = (m_y - side_bumper - header) // box_height
    box_col = (m_x - side_bumper) // box_width

    # convert to the number of the box used when drawing the window
    box_num = int(box_col) + (int(box_row) * cols)

    return box_num

def get_xy_from_box(box_num):

    box_xpos = (side_bumper + ((box_num % cols) * box_width))
    box_ypos = (side_bumper + header + ((box_num // cols) * box_height))

    return box_xpos, box_ypos

def draw_char_on_win(box_num, char, num_mines = False):

    # pygame.draw.circle(win, (0, 0, 0), (x,y), radius, 3)
    letter_font = pygame.font.SysFont('Helvetica', 30)
    if num_mines:
        text = letter_font.render(char, 1, (reds[num_mines],0,0))
    elif str(num_mines) == '0':
        return
    else:
        text = letter_font.render(char, 1, (0,0,0))
    box_xpos, box_ypos = get_xy_from_box(box_num)

    win.blit(text, (box_xpos + 4, box_ypos + 1))

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
    
    win.fill((greys[1], greys[1], greys[1])) # RGB color in tuple

    line_weight = 3

    # create outer box first
    # Rect object: Rect(left, top, width, height)
    # button_box = pygame.Rect(side_bumper - line_weight, side_bumper - line_weight, width - (2 * side_bumper) + line_weight, height - (2 * side_bumper)  + line_weight)
    # pygame.draw.rect(win, (0,0,0), button_box, width=3)

    for i in range(num_boxes):
        box_xpos = side_bumper + ((i % cols) * box_width)
        box_ypos = side_bumper + header + ((i // cols) * box_height)

        clicked_box_pos_only = [i[0] for i in clicked_boxes]

        if i in clicked_box_pos_only or i == click_and_held_box:
            button_box = pygame.Rect(box_xpos, box_ypos, box_width, box_height)
            pygame.draw.rect(win, (greys[0],greys[0],greys[0]), button_box)

            button_border = pygame.Rect(box_xpos, box_ypos, box_width, box_height)
            pygame.draw.rect(win, (greys[1], greys[1], greys[1]), button_border, width=1)
        
        else:
            # draw boxes with lines to get feeling of depth: 
            # white-ish lines for left
            pygame.draw.line(win, (greys[2], greys[2], greys[2]), (box_xpos, box_ypos), (box_xpos + box_width, box_ypos), line_weight)

            # top line
            pygame.draw.line(win, (greys[2], greys[2], greys[2]), (box_xpos, box_ypos), (box_xpos, box_ypos + box_height), line_weight)

            # darker grey lines for bottom
            pygame.draw.line(win, (greys[0], greys[0], greys[0]), (box_xpos + line_weight, box_ypos + box_height - line_weight), (box_xpos + box_width - line_weight, box_ypos + box_height - line_weight), line_weight)
            
            # right line
            pygame.draw.line(win, (greys[0], greys[0], greys[0]), (box_xpos + box_width - 3, box_ypos + line_weight), (box_xpos + box_width - 3, box_ypos + box_height - line_weight), line_weight)

            button_border = pygame.Rect(box_xpos, box_ypos, box_width, box_height)
            pygame.draw.rect(win, (0,0,0), button_border, width=1)
        
    for i, num_mines in clicked_boxes:
        draw_char_on_win(i, chr(48 + num_mines), num_mines)
    
    if display_mines:
        for i in mine_locations:
            draw_char_on_win(i, chr(88))
    else:
        for i in clicked_flags:
            draw_char_on_win(i, chr(63))

    header_font = pygame.font.SysFont('Helvetica', 25)
    header_text = header_font.render(str(num_total_mines - len(clicked_flags)), 1, (150,0,0))
    win.blit(header_text, (600, 20))
    # submit_text = letter_font.render('SUBMIT', 1, (0,0,0))
    # win.blit(submit_text, (625, 260))

    pygame.display.update()


def main(): 
    fps = 60
    clock = pygame.time.Clock()
    run = True

    # start game with randomly-generated mine locations
    global mine_locations, num_total_mines
    num_total_mines = 100
    mine_locations = []

    while run:
        clock.tick(fps)
        
        draw_window()

        button_mods = pygame.key.get_mods()

        if pygame.mouse.get_pressed()[0] and (not button_mods or button_mods % 64 != 0):
                m_x, m_y = pygame.mouse.get_pos()
                box_num = get_box_from_click(m_x, m_y)

                clicked_box_pos_only = [i[0] for i in clicked_boxes]

                if box_num != 'border' and box_num not in clicked_box_pos_only:

                    box_xpos, box_ypos = get_xy_from_box(box_num)

                    button_box = pygame.Rect(box_xpos, box_ypos, box_width, box_height)
                    pygame.draw.rect(win, (greys[0],greys[0],greys[0]), button_box)

                    button_border = pygame.Rect(box_xpos, box_ypos, box_width, box_height)
                    pygame.draw.rect(win, (greys[1], greys[1], greys[1]), button_border, width=1)

                    global click_and_held_box
                    click_and_held_box = box_num

                    pygame.display.update()
                
                else:
                    click_and_held_box = -1
                

        else:
            click_and_held_box = -1
            pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            

            if event.type == pygame.MOUSEBUTTONUP and (not button_mods or button_mods % 64 != 0):
                m_x, m_y = pygame.mouse.get_pos()
                box_num = get_box_from_click(m_x, m_y)

                # check if click within boxes
                if box_num != 'border':

                    if not mine_locations:
                        # global mine_locations
                        mine_locations = generate_opening_mines(box_num, num_total_mines)

                    if box_num in mine_locations:
                        global display_mines
                        display_mines = True
                        
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
                    
            elif event.type == pygame.MOUSEBUTTONDOWN and button_mods and button_mods % 64 == 0: # ctrl click
                m_x, m_y = pygame.mouse.get_pos()
                box_num = get_box_from_click(m_x, m_y)

                clicked_box_pos_only = [i[0] for i in clicked_boxes]

                # check if click within boxes and not already clicked
                if box_num != 'border' and box_num not in clicked_box_pos_only:
                    clicked_flags.append(box_num)



if __name__ == '__main__':

    status = True
    while status:
        status = main()

pygame.quit()