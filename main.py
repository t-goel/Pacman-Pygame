import copy
import random
import sys
import time

import pygame

pygame.init()
screen = pygame.display.set_mode([0, 0])
clock = pygame.time.Clock()
running = True
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

screen_width = 700
screen_height = 775
tile_size = 25

def death():
    screen.fill((0,0,0))
    # screen.blit('redghost.png',(pacman.rect.x,pacman.rect.y))
    pygame.display.update()

screen = pygame.display.set_mode([0, 0])

original_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def quit_game(file):
    fin = open(file, "r")
    x = int(fin.read())
    fin.close()
    if len(world.dot_list) == 0:
        if count < x:
            fout = open(file, "w")
            fout.truncate(0)
            fout.write(str(count))
            fout.close()
            print("NEW HIGH SCORE: ", str(count))
            print(f"The previous high score was {str(x)}.")


        if count > x:
            print(f"The current high score is {str(x)}.")
            print("Your score was " + str(count) + " :(")

    else:
        print("GAME OVER.")



class World():
    def __init__(self, data):
        self.tile_list = []
        self.dot_list = []
        border_img = pygame.image.load("media/wall.png")
        dot_img = pygame.image.load("media/dot.png")
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(border_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 0:
                    img = pygame.transform.scale(dot_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.dot_list.append(tile)
                col_count += 1
            row_count += 1
        # print(len(self.dot_list))
        x = len(self.dot_list)

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
        for tile in self.dot_list:
            screen.blit(tile[0], tile[1])


class Pacman():
    def __init__(self, x, y, direction):
        img = pygame.image.load("media/imageR.jpg")
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction

    def update(self):
        px = self.rect.x
        py = self.rect.y
        # movement is by pixels, 25 by 25
        key = pygame.key.get_pressed()
        # first if statement makes it so that pacman doesn't get stuck
        try:
            if world_data[int(py / 25)][int(px / 25) - 1] != 1:
                if key[pygame.K_LEFT]:
                    img = pygame.image.load("media/imageL.jpg")
                    self.image = pygame.transform.scale(img, (tile_size, tile_size))
                    self.direction = "L"
            if world_data[int(py / 25)][int(px / 25) + 1] != 1:
                if key[pygame.K_RIGHT]:
                    img = pygame.image.load("media/imageR.jpg")
                    self.image = pygame.transform.scale(img, (tile_size, tile_size))
                    self.direction = "R"
            if world_data[int(py / 25) - 1][int(px / 25)] != 1:
                if key[pygame.K_UP]:
                    img = pygame.image.load("media/imageU.jpg")
                    self.image = pygame.transform.scale(img, (tile_size, tile_size))
                    self.direction = "U"
            if world_data[int(py / 25) + 1][int(px / 25)] != 1:
                if key[pygame.K_DOWN]:
                    img = pygame.image.load("media/imageD.jpg")
                    self.image = pygame.transform.scale(img, (tile_size, tile_size))
                    self.direction = "D"
        except IndexError:
            # im too lazy to fix this
            pass
        if self.direction == "R":
            px += 25
        if self.direction == "L":
            px -= 25
        if self.direction == "D":
            py += 25
        if self.direction == "U":
            py -= 25

        # teleportation
        if px == 700 and py == 350 and self.direction == "R":
            px = 0
            py = 350
        if px == -25 and py == 350 and self.direction == "L":
            px = 675
            py = 350

        if world_data[int((py / 25))][int((px / 25))] != 1:
            self.rect.x = px
            self.rect.y = py

            world_data[int((self.rect.y / 25))][int((self.rect.x / 25))] = 2

        screen.blit(self.image, self.rect)

#spent 3 hours on this
class Ghost():
    def __init__(self, x, y, direction, colorfile):
        img = pygame.image.load(colorfile)
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction

    def update(self):
        px = self.rect.x
        py = self.rect.y
        directions = ['U', 'D', 'R', 'L']
        if self.rect.x == pacman.rect.x and self.rect.y == pacman.rect.y:
            quit_game('high_score.txt')
            sys.exit()

        try:
            lcheck = world_data[int(py / 25)][int(px / 25) - 1] != 1
            rcheck = world_data[int(py / 25)][int(px / 25) + 1] != 1
            dcheck = world_data[int(py / 25) + 1][int(px / 25)] != 1
            ucheck = world_data[int(py / 25) - 1][int(px / 25)] != 1
        except IndexError:
            pass
        # first instance not on wall
        if (self.direction == "L" and lcheck) or (self.direction == 'R' and rcheck):
            if ucheck:
                self.direction = random.choice([self.direction, self.direction, 'U'])

            if dcheck:
                self.direction = random.choice([self.direction, self.direction, 'D'])
        elif (self.direction == "U" and ucheck) or (self.direction == 'D' and dcheck):
            if rcheck:
                self.direction = random.choice([self.direction, self.direction, 'R'])

            if lcheck:
                self.direction = random.choice([self.direction, self.direction, 'L'])

        # if ghost has a wall in front
        elif (self.direction == "L" and not lcheck) or (self.direction == 'R' and not rcheck):
            if ucheck and dcheck:
                self.direction = random.choice(["U", "D"])
            elif ucheck:
                self.direction = "U"
            elif dcheck:
                self.direction = "D"

        elif (self.direction == "U" and not ucheck) or (self.direction == 'D' and not dcheck):
            if rcheck and lcheck:
                self.direction = random.choice(["R", "L"])
            elif rcheck:
                self.direction = "R"
            elif lcheck:
                self.direction = "L"

        if self.direction == "R":
            px += 25
        if self.direction == "L":
            px -= 25
        if self.direction == "D":
            py += 25
        if self.direction == "U":
            py -= 25

        if px == 675 and py == 350 and self.direction == "R":
            px = 0
            py = 350
        if px == -25 and py == 350 and self.direction == "L":
            px = 650
            py = 350

        if world_data[int((py / 25))][int((px / 25))] != 1:
            self.rect.x = px
            self.rect.y = py

        screen.blit(self.image, self.rect)

        if self.rect.x == pacman.rect.x and self.rect.y == pacman.rect.y:
            quit_game('high_score.txt')
            sys.exit()


pacman = Pacman(25, 25, "R")

tim = Ghost(225, 450, "D", 'media/redghost.png')
pinky = Ghost(225, 250, "R", 'media/pinkghost.png')
matt = Ghost(450, 450, "L", 'media/cyanghost.png')
clyde = Ghost(450, 250, "D", 'media/orangeghost.png')

if __name__ == "__main__":
    global SCREEN, CLOCK
    pygame.init()
    pygame.display.set_mode((screen_width, screen_height))

    background = (0, 0, 0)
    screen.fill(background)
    pygame.display.set_caption("PacMan")
    pygame_icon = pygame.image.load('media/icons8-pacman-100.png')
    pygame.display.set_icon(pygame_icon)
    world_data = copy.deepcopy(original_map)
    world = World(world_data)
    world.draw()
    running = True
    count = 0

    while True:

        count += 1
        pygame.time.delay(120)
        screen.fill((0, 0, 0))
        world = World(world_data)
        world.draw()

        tim.update()
        pinky.update()
        matt.update()
        clyde.update()
        pacman.update()

        for event in pygame.event.get():
            # escape
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    quit_game('high_score.txt')
                    sys.exit()
            # for continuous running
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_r:
            #         world_data = copy.deepcopy(original_map)
            #         world = World(world_data)
            #         pacman = Pacman(25, 25, "R")
            #         count = 0
            # running = False

            if event.type == pygame.QUIT:
                #quit_game('high_score.txt')
                sys.exit()
        if len(world.dot_list) == 0:
            print("GAME OVER!")

           # quit_game('high_score.txt')
            sys.exit()

        pygame.display.update()
