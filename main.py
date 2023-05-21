from pygame import *

win_width =600
win_height = 500

dx = 5
dy = 5

window = display.set_mode((win_width,win_height))
display.set_caption('Ping pong')
background = transform.scale(image.load('wall.jpg'),(win_width,win_height))

game = True
clock = time.Clock()
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move_3(self):
        self.rect.x += dx
        self.rect.y += dy

class Rocket(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= 1
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += 1

    def move_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y> 0:
            self.rect.y -= 1
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += 1

rocket1 =  Rocket('Rocket.png', 30, 200, 50, 150, 10)
rocket2 =  Rocket('Rocket.png', 519, 200, 50, 150, 10)
ball = GameSprite('Ball.png', 100,300, 50, 50, 1)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:


        if sprite.collide_rect(ball, rocket1) or sprite.collide_rect(ball, rocket2):
            dx *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:

            dy *= -1
        if ball.rect.x < 0:
            finish = True
        if ball.rect.x < 0:
            finish = True

        window.blit(background, (0, 0))
        rocket1.reset()
        rocket1.move_2()
        rocket2.reset()
        rocket2.move()
        ball.reset()
        ball.rect.x += dx
        ball.rect.y += dy

    display.update()
    clock.tick(60)
