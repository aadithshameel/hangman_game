import pygame
import math
import random

# Setting up Display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Play Hangman!")

FPS = 60
clock = pygame.time.Clock()

# Game Variables
hangman_status = 0
words = ["PYTHON","JAVASCRIPT","IDE","APPLE","GOOGLE","AMAZON","NETFLIX","FACEBOOK"]
word = random.choice(words)
guessed = []

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# Button Variables
GAP = 15
RADIUS = 20
startX = round((WIDTH - (GAP + RADIUS * 2) * 13) / 2)
startY = 400
letters = []
A = 65
for i in range(26):
    x_coord = startX + GAP * 2 + (GAP + RADIUS * 2) * (i % 13)
    y_coord = startY + (i // 13) * (GAP + RADIUS * 2)
    letters.append([x_coord, y_coord, chr(A + i), True])

# Loading Images
images = []
for i in range(6):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)


# Drawing Buttons
def draw():
    win.fill(WHITE)
    # Title Screen
    text = TITLE_FONT.render("Play Hangman", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    # Draw Letters
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word = display_word + letter + " "
        else:
            display_word = display_word + "_ "
        text = WORD_FONT.render(display_word, 1, BLACK)
        win.blit(text, (400, 200))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


# Displaying Message
def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width() / 2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


# Game Loop
run = True
while run:
    clock.tick(FPS)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status = hangman_status + 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("You Won!")
        break
    if hangman_status == 6:
        display_message("You Lost!")
        break
pygame.quit()
