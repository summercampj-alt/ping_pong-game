from pygame import *
from random import randint

# Setup fonts for text
font.init()
font1 = font.SysFont('Arial', 80)
font2 = font.SysFont('Arial', 36)
im_back = "background.jpg"

# Text displays
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose1 = font1.render('PLAYER 2 WINS!', True, (180, 0, 0)) 
lose2 = font1.render('PLAYER 1 WINS!', True, (180, 0, 0)) 

# Game scores
score = 0 
speed_x = 3
speed_y = 3

# Parent class for game objects
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 200: 
            self.rect.y += self.speed
            
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 200: 
            self.rect.y += self.speed

# Create display window
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))

racket1 = Player('rectangle.png', 30, 200, 50, 200, 10)
racket2 = Player('rectangle.png', 620, 200, 50, 200, 10) 

# CORRECTION ICI : Utilisation du nom exact visible sur votre écran
ball = GameSprite('ball (2).png', 200, 200, 40, 40, 7) 

background = transform.scale(image.load(im_back), (win_width, win_height))

# Light blue background color
LIGHT_BLUE = (173, 216, 230)

# Game status flags
finish = False
run = True
clock = time.Clock()
FPS = 60

# Main game loop
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
              
    window.fill(LIGHT_BLUE)
    window.blit(background, (0, 0))

    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > win_height - 40 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True

        if ball.rect.x > win_width:
            finish = True

        racket1.update_l()
        racket2.update_r()

    racket1.reset()
    racket2.reset()
    ball.reset()

    if finish:
        if ball.rect.x < 0:
            window.blit(lose1, (120, 200))
        else:
            window.blit(lose2, (120, 200))

    display.update()
    clock.tick(FPS)
