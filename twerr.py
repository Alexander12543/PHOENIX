from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] :
            self.rect.x -= self.speed
        if keys[K_RIGHT]  :
            self.rect.x += self.speed
        if keys[K_UP] :
            self.rect.y -= self.speed
        if keys[K_DOWN] :
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"


win_width=700
win_height=500       
background = transform.scale(image.load("1.png"), (win_width, win_height))
w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 200, 130, 10, 350)
w5 = Wall(154, 205, 50, 450, 130, 10, 360)
w6 = Wall(154, 205, 50, 300, 20, 10, 350)
w7 = Wall(154, 205, 50, 390, 120, 130, 10)

packman = Player('9.jpg', 5, win_height - 80, 4)
monster = Enemy('9.jpg', win_width - 80, 280, 2)
final = GameSprite('9.jpg', win_width - 120, win_height - 80, 0)


window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("1.png"), (700, 500))

x1 = 100
y1 = 300
x2 = 300
y2 = 300


game = True 
clock = time.Clock()
speed = 9
FPS = 60
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

  

    if game == True:
        window.blit(background,(0, 0))
        packman.reset()
        monster.reset()
        packman.update()
        monster.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
    if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3) or sprite.collide_rect(packman, w4) or sprite.collide_rect(packman, w5) or sprite.collide_rect(packman, w6) or sprite.collide_rect(packman, w7):
        finish = True
        window.blit(lose, (200, 200))
   
    if sprite.collide_rect(packman, final):
        game = False
        window.blit(win, (200, 200))

    display.update()
