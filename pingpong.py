
from pygame import *
from random import randint

# Setup fonts for text
font.init()
font1 = font.SysFont('Arial', 80)
font2 = font.SysFont('Arial', 36)
im_back = "background.jpg"

# Text displays
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

# Game scores
score = 0 

# Parent class for game objects
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        # For Ping-Pong, we can use simple colored rectangles or images
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Main player class (Paddle)
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        # Left paddle controls (example using W and S)
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        # Left paddle controls (example using W and S)
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

# Create display window
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))

racket1 = Player('rectangle.png', 30, 200, 50, 200, 10)
racket2 = Player('rectangle.png', 650, 200, 50, 200, 10)
background = transform.scale(image.load(im_back), (win_width, win_height))

# Light blue background color
LIGHT_BLUE = (173, 216, 230)

# Game status flags
finish = False
run = True

# Main game loop
while run:
    # Check for window exit button click
    for e in event.get():
        if e.type == QUIT:
            run = False
              
    if not finish:
        # Fill screen with light blue background
        window.fill(LIGHT_BLUE)

        # Write score text on the screen
        
        window.blit(background,(0,0))
        racket1.reset()
        racket1.update_l()

        racket2.reset()
        racket2.update_r()

        display.update()

    time.delay(50)

