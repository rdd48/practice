"""This 'solution' was inspired heavily from https://github.com/Valokoodari/advent-of-code/blob/main/2021/23.py
Basically, this turns day 23's problem into a game that can be solved... didn't think through how to solve thru
trying all solutions in code."""


import pygame


pygame.init()

# global varaibles for window
width, height = 800, 550
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Amphipods")

# global variables for boxes
header = 50
side_bumper = 10
cols = 11
box_width = (width - (2 * side_bumper)) / cols
box_height = box_width
line_weight = 2

# list will contain amphipod instances
amphipods = []

# score
scores = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}


# global variables for positioning
pos_1 = {
    2: ['A', 'D'],
    4: ['C', 'D'],
    6: ['B', 'A'],
    8: ['B', 'C']
}

pos_2 = {
    2: ['A', 'D', 'D', 'D'],
    4: ['C', 'C', 'B', 'D'],
    6: ['B', 'B', 'A', 'A'],
    8: ['B', 'A', 'C', 'C']
}

unicodes = {
    'A': 65,
    'B': 66,
    'C': 67,
    'D': 68,
}

class Amphipod:
    def __init__(self, char, start_xpos, start_ypos, selected):
        self.char = char
        self.xpos = start_xpos # row
        self.ypos = start_ypos # col
        self.selected = selected
    
    def reselect(self):
        if self.selected == True:
            self.selected = False
        else:
            self.selected = True
    
    def move_up(self):
        self.ypos -= 1

    def move_down(self):
        self.ypos += 1

    def move_left(self):
        self.xpos -= 1

    def move_right(self):
        self.xpos += 1


def reselect_amphipod():
    amphipods_copy = amphipods.copy()
    amph_deselect = amphipods_copy[sele]
    amph_deselect.reselect()
    amphipods[sele] = amph_deselect

    next_pos = sele + 1 if sele < len(amphipods_copy) - 1 else 0
    amph_select = amphipods_copy[next_pos]
    amph_select.reselect()
    amphipods[next_pos] = amph_select

def move_amphipod(dir, total_score):
    amph_moving = amphipods[sele]
    if dir == 'up':
        if amph_moving.ypos > 0:
            if not occupied[(amph_moving.xpos, amph_moving.ypos - 1)]:
                occupied[(amph_moving.xpos, amph_moving.ypos)] = False
                occupied[(amph_moving.xpos, amph_moving.ypos - 1)] = True
                amph_moving.move_up()
                total_score += scores[amph_moving.char]

    elif dir == 'down':
        if amph_moving.ypos < 2 and amph_moving.xpos in (2, 4, 6, 8): # need to update for round 2
            if not occupied[(amph_moving.xpos, amph_moving.ypos + 1)]:
                occupied[(amph_moving.xpos, amph_moving.ypos)] = False
                occupied[(amph_moving.xpos, amph_moving.ypos + 1)] = True
                amph_moving.move_down()
                total_score += scores[amph_moving.char]

    elif dir == 'left':
        if amph_moving.xpos > 0 and amph_moving.ypos == 0: 
            if not occupied[(amph_moving.xpos - 1, amph_moving.ypos)]:
                occupied[(amph_moving.xpos, amph_moving.ypos)] = False
                occupied[(amph_moving.xpos - 1, amph_moving.ypos)] = True
                amph_moving.move_left()
                total_score += scores[amph_moving.char]

    elif dir == 'right':
        if amph_moving.xpos < 10 and amph_moving.ypos == 0:
            if not occupied[(amph_moving.xpos + 1, amph_moving.ypos)]:
                occupied[(amph_moving.xpos, amph_moving.ypos)] = False
                occupied[(amph_moving.xpos + 1, amph_moving.ypos)] = True
                amph_moving.move_right()
                total_score += scores[amph_moving.char]
    
    return total_score



def draw_char_on_win(amph):
    letter_font = pygame.font.SysFont('Helvetica', 55)
    color = (0, 255, 0) if amph.selected else (255, 255, 255)   
    text = letter_font.render(amph.char, 1, color)

    xpos = side_bumper + ((amph.xpos % cols) * box_width) + 10
    ypos = side_bumper + header + ((amph.xpos // cols) * box_height) + ((amph.ypos) * (side_bumper + box_height)) + 10

    win.blit(text, (xpos, ypos))


def draw_window(game_started, total_score):
    win.fill((16, 12, 36))

    score_font = pygame.font.SysFont('Helvetica', 35)
    score_text = score_font.render(f'Score: {total_score}', 1, (255, 255, 255))
    # score_text = score_font.render(f"Score: {score}", True, Color.TEXT_WHITE)
    win.blit(score_text, (15, 15))

    for i in range(cols):
        box_xpos = side_bumper + ((i % cols) * box_width)
        box_ypos = side_bumper + header + ((i // cols) * box_height)

        button_border = pygame.Rect(box_xpos, box_ypos, box_width-side_bumper, box_height)
        pygame.draw.rect(win, (0, 0, 18), button_border)
        pygame.draw.rect(win, (120, 120, 120), button_border, width=1)

        if i in (2, 4, 6, 8):
            num_cols = 2 if round_num == 1 else 4
            for j in range(num_cols):
                low_box_ypos = box_ypos + ((j+1) * (side_bumper + box_height))
                lower_button = pygame.Rect(box_xpos, low_box_ypos, box_width-side_bumper, box_height)
                pygame.draw.rect(win, (0, 0, 18), lower_button)
                pygame.draw.rect(win, (120, 120, 120), lower_button, width=1)

                if not game_started:
                    dec_val = pos_1[i][j] if round_num == 1 else pos_2[i][j]
                    selected = True if i == 2 and j == 0 else False
                    amph = Amphipod(chr(unicodes[dec_val]), i, j+1, selected)
                    amphipods.append(amph)
                
        for amph in amphipods:
            draw_char_on_win(amph)
                    
    pygame.display.update()



if __name__ == '__main__':

    fps = 60
    clock = pygame.time.Clock()
    run = True
    game_started = False

    total_score = 0
    round_num = 1

    while run:
        draw_window(game_started, total_score)

        if not game_started:
            global sele
            sele = 0

            occupied = {(x, 0): False for x in range(11)}
            for row in (2,4,6,8):
                if round_num == 1:
                    for col in range(1,3):
                        occupied[(row, col)] = True
                elif round_num == 2:
                    for col in range(1,5):
                        occupied[(row, col)] = True
            
            game_started = True

        clock.tick(fps)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    reselect_amphipod()
                    if sele < len(amphipods) - 1:
                        sele += 1
                    else:
                        sele = 0
                elif event.key == pygame.K_UP:
                    total_score = move_amphipod('up', total_score)
                elif event.key == pygame.K_DOWN:
                    total_score = move_amphipod('down', total_score)
                elif event.key == pygame.K_LEFT:
                    total_score = move_amphipod('left', total_score)
                elif event.key == pygame.K_RIGHT:
                    total_score = move_amphipod('right', total_score)

                # reset game
                elif event.key == pygame.K_1:
                    amphipods = []
                    total_score = 0
                    game_started = False

                
                elif event.key == pygame.K_2:
                    amphipods = []
                    total_score = 0
                    game_started = False
                    round_num = 2
