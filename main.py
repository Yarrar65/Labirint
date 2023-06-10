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

window = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
clock = pygame.time.Clock()

game = True
level = 1 
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    clock.tick(FPS)
    pygame.display.update()
    
