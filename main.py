from typing import Any
import pygame
pygame.init()
import os
from  random import shuffle, choice

def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, file_name)
    return path

WIN_WIDTH = 1200
WIN_HEIGHT = 700
FPS = 40

back = pygame.image.load(file_path(r"images\back.jpg"))
back = pygame.transform.scale(back, (WIN_WIDTH,WIN_HEIGHT))
image_win = pygame.image.load(file_path(r"images\mouse_happy.png"))
image_win = pygame.transform.scale(image_win, (WIN_WIDTH,WIN_HEIGHT))
image_lose = pygame.image.load(file_path(r"images\you_lose.png"))
image_lose = pygame.transform.scale(image_lose, (WIN_WIDTH,WIN_HEIGHT))

pygame.mixer.music.load(file_path(r"music\5fee5524b9c82f3.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

music_key = pygame.mixer.Sound(file_path(r"music\zvuk-otveta-5fsd5.ogg"))
musik_chests = pygame.mixer.Sound(file_path(r"music\Minecraft-Chest-Opening-QuickSounds.com.ogg"))

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
        self.direction = "right"
        self.image_r = self.image
        self.image_l = pygame.transform.flip(self.image, True,False)
        self.key_color = None

    def update(self):
        if self.speedx < 0 and self.rect.left > 0 or self.speedx > 0 and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speedx
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if  self.speedx < 0:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)
        if  self.speedx > 0:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left)

        if self.speedy < 0 and self.rect.top > 0 or self.speedy > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speedy

        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if  self.speedy < 0:
            for wall in walls_touched:
                self.rect.top = max(self.rect.top, wall.rect.bottom)
        if  self.speedy > 0:
            for wall in walls_touched:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)

class Color_sprite(Game_sprite):
    def __init__(self, x, y, width, height, image, color):
        super().__init__(x, y, width, height, image)
        self.color = color

class Enemy(Game_sprite):
    def __init__(self, x, y, width, height, image, speed, direction, xmin, xmax):
        super().__init__(x, y, width, height, image)
        self.speed = speed
        self.direction = direction
        self.xmin = xmin
        self.xmax = xmax
        self.image_r = self.image
        self.image_l = pygame.transform.flip(self.image, True, False)
        

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.right >= self.xmax:
            self.direction = "left"
            self.speed += 0.5
            self.image = self.image_l
        if self.rect.left <= self.xmin:
            self.direction = "right"
            self.speed += 0.5
            self.image = self.image_r
        
        

        


player = Player(4, 4, 70, 40, r"images/souris_02-300x258.png")
enemy = Enemy(250, 260, 100, 100, r"images/Eurasian_Lynx.png", 2, "right", 250, 1100 )
finish = Game_sprite(-600, 630, 70, 50, r"images/cheese-1.png")
fail = Game_sprite(450, 610, 50, 50, r"images\pngimg.com - mouse_trap_PNG16.png")

chests_x = [590,400,230,790,990]
shuffle(chests_x)
colors = ["brown","blue","yellow","red","green"]
shuffle(colors)
colors_images = {
    "brown": r"images\Crypto_key.png",
    "yellow": r"images\Yellow_key.png",
    "blue": r"images\Blue_key.png",
    "red": r"images\Red_key.png",
    "green": r"images\green_key.png",
}

keys  = pygame.sprite.Group()
color = choice(colors)
colors.remove(color)
key1 = Color_sprite(100, 100, 100, 50, colors_images[color], color)
keys.add(key1)


chests = pygame.sprite.Group()
chest1 = Color_sprite(chests_x[0], 600, 110, 110, r"images\Chest.png", "brown")
chests.add(chest1)
chest2 = Color_sprite(chests_x[1], 600, 110, 110, r"images\Chest_blue.png", "blue")
chests.add(chest2)
chest3 = Color_sprite(chests_x[2], 600, 110, 110, r"images\Chest_yellow.png","yellow")
chests.add(chest3)
chest4 = Color_sprite(chests_x[3], 600, 110, 110, r"images\Chest_red.png", "red")
chests.add(chest4)
chest4 = Color_sprite(chests_x[4], 600, 110, 110, r"images\Chest_green.png","green")
chests.add(chest4)




walls = pygame.sprite.Group()
wall1 = Game_sprite(200, 200, 300, 10, r"images/product-3101010161.jpg")
walls.add(wall1)
wall2 = Game_sprite(200, 200, 10, 300, r"images/product-3101010161.jpg")
walls.add(wall2)
wall3 = Game_sprite(350, 400, 10, 300, r"images/product-3101010161.jpg")
walls.add(wall3)
wall4 = Game_sprite(200, 400, 10, 300, r"images/product-3101010161.jpg")
walls.add(wall4)
wall5 = Game_sprite(530, 400, 10, 300, r"images/product-3101010161.jpg")
walls.add(wall5)
wall6 = Game_sprite(730, 400, 10, 300, r"images/product-3101010161.jpg")
walls.add(wall6)
wall7 = Game_sprite(930, 400, 10, 300, r"images/product-3101010161.jpg")
walls.add(wall7)
wall8 = Game_sprite(1130, 200, 10, 600, r"images/product-3101010161.jpg")
walls.add(wall8)
wall9 = Game_sprite(700, 200, 450, 10, r"images/product-3101010161.jpg")
walls.add(wall9)


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
                    player.direction = "right"
                    player.image = player.image_r
                if event.key == pygame.K_a:
                    player.speedx = -5
                    player.direction = "left"
                    player.image = player.image_l
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
        enemy.update()
        finish.show()
        walls.draw(window)
        #fail.show()
        chests.draw(window)
        keys.draw(window)


        key = pygame.sprite.spritecollide(player, keys, True)
        if key:
            player.key_color = key[0].color
            music_key.play()
        
        chests_toched = pygame.sprite.spritecollide(player, chests, False)
        if chests_toched:
            if player.key_color == chests_toched[0].color:
                musik_chests.play()
                chests_toched[0].kill()

                player.rect.x = 4
                player.rect.y = 4 

                if len(colors) > 0:
                    color = choice(colors)
                    colors.remove(color)
                    x = chests_toched[0].rect.x
                    y = chests_toched[0].rect.y + 10
                    key1 = Color_sprite(x, y, 100, 50, colors_images[color], color)
                    keys.add(key1)
                else:
                    x = chests_toched[0].rect.x
                    y = chests_toched[0].rect.y + 10
                    finish.rect.x = x
                    finish.rect.y = y

        if pygame.sprite.collide_rect(player,finish):
            level = 10
            pygame.mixer.music.load(file_path(r"music\583699913672e65.mp3"))
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1)

        if pygame.sprite.collide_rect(player,enemy):
            level = 11
            pygame.mixer.music.load(file_path(r"music\us.ogg"))
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()


    elif level == 10:
        window.blit(image_win, (0, 0))

    elif level == 11:
        window.blit(image_lose, (0, 0))


                



            

    clock.tick(FPS)
    pygame.display.update()

