import pygame
pygame.init()
import os

def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, file_name)
    return path

WIN_WIDTH = 1200
WIN_HEIGHT = 700
FPS = 40

back = pygame.image.load(file_path(r"images\back.jpg"))
back = pygame.transform.scale(back, (WIN_WIDTH,WIN_HEIGHT))

window = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
clock = pygame.time.Clock()

class Game_sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width,height))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))

class Player(Game_sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        


player = Player(4, 4, 70, 40, r"images/souris_02-300x258.png")
enemy = Game_sprite(50, 60, 100, 100, r"images/Eurasian_Lynx.png")
finish = Game_sprite(100, 200, 70, 50, r"images/cheese-1.png")


game = True
level = 1 
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if level == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.speedx = 5
                if event.key == pygame.K_a:
                    player.speedx = -5
                if event.key == pygame.K_w:
                    player.speedy = -5
                if event.key == pygame.K_s:
                    player.speedy = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.speedx = 0
                if event.key == pygame.K_a:
                    player.speedx = 0
                if event.key == pygame.K_w:
                    player.speedy = 0
                if event.key == pygame.K_s:
                    player.speedy = 0

    if level == 1:
        window.blit(back, (0, 0))
        player.show()
        player.update()
        enemy.show()
        finish.show()

    clock.tick(FPS)
    pygame.display.update()

