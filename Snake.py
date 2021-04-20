import pygame
import random
import math

# Init Pygame
pygame.init()

# Clock
clock = pygame.time.Clock()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")

# Sprite class
class Sprite:
    length = 1
    lastx = []
    lasty = []

    def __init__(self, length, color, x_pos, y_pos, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos

    def Player(self):
        pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height))
        Sprite.lastx.append(self.x_pos)
        Sprite.lasty.append(self.y_pos)

        if len(Sprite.lastx) > 1000 or len(Sprite.lasty) > 1000:
            Sprite.lastx.pop(0)
            Sprite.lasty.pop(0)

        for i in range(1, Sprite.length + 1):
            pygame.draw.rect(screen, self.color, (Sprite.lastx[-i], Sprite.lasty[-i], self.width, self.height))

    def Food(self):
        pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height))

    @staticmethod
    def collision(a, b, c, d):
        dist = math.sqrt(((a - b) ** 2) +((c - d) ** 2))
        if dist < 40:
            global score
            score += 1
            Sprite.length += 1
            food.x_pos = random.randint(0, 19) * 40
            food.y_pos = random.randint(0, 14) * 40

# Player
playerx = 360
playery = 280
player_color = (0, 255, 0)
player_width = 40
player_height = 40
player_length = 0
x_change = 0
y_change = 0
snake = Sprite(player_length, player_color, playerx, playery, player_width, player_height)

# food
foodx = random.randint(0,19) * 40
foody = random.randint(0, 14) * 40
food_color = (255, 0, 0)
food_width = 40
food_height = 40
food_length = 1
food = Sprite(food_length, food_color, foodx, foody, food_width, food_height)

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10
def show_score(x, y):
    score_show = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_show, (x, y))

# Game Loop
running = True
while running:
    clock.tick(5)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # up or down
            if event.key == pygame.K_UP:
                if y_change == 0:
                    y_change = -40
                    x_change = 0

            if event.key == pygame.K_DOWN:
                if y_change == 0:
                    y_change = 40
                    x_change = 0

            # left or right
            if event.key == pygame.K_RIGHT:
                if x_change == 0:
                    x_change = 40
                    y_change = 0

            if event.key == pygame.K_LEFT:
                if x_change == 0:
                    x_change = -40
                    y_change = 0

    # Boundaries collision
    if snake.x_pos < 0 or snake.x_pos > 760:
        running = False

    elif snake.y_pos > 560 or snake.y_pos < 0:
        running = False

    # Snake collision
    for i in range(1, Sprite.length):
        if snake.x_pos == Sprite.lastx[-i] and snake.y_pos == Sprite.lasty[-i]:
            running = False

    Sprite.Food(food)
    Sprite.Player(snake)
    Sprite.collision(food.x_pos, snake.x_pos, food.y_pos, snake.y_pos)
    snake.x_pos += x_change
    snake.y_pos += y_change
    show_score(text_x, text_y)

    pygame.display.update()
