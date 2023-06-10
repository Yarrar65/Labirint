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

        
player = Game_sprite(4, 4, 50, 20, r"images\back.jpg")


game = True
level = 1 
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if level == 1:
        window.blit(back, (0, 0))
        player.show()

    clock.tick(FPS)
    pygame.display.update()

