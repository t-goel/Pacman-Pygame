import copy
import random
import sys
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from q_learning import Q, save_q_table, get_state, epsilon_greedy, get_reward, update_q

pygame.init()
screen = pygame.display.set_mode([0, 0])
clock = pygame.time.Clock()
running = True

screen_width = 700
screen_height = 775
tile_size = 25

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

            for dot in world.dot_list[:]:  # iterate over a copy
                if self.rect.colliderect(dot[1]):
                    world.dot_list.remove(dot)

        screen.blit(self.image, self.rect)


class Ghost():
    def __init__(self, x, y, direction, colorfile):
        img = pygame.image.load(colorfile)
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction

    def update(self):
        global running

        if self == matt:
            state = get_state(self, pacman, tile_size)
    
            # Pick an action with epsilon-greedy
            action = epsilon_greedy(state, epsilon=0.2)

            # Attempt move
            valid_move = True
            new_x, new_y = self.rect.x, self.rect.y
            if action == "U":
                new_y -= 25
                if world_data[new_y // 25][new_x // 25] == 1:
                    valid_move = False
            elif action == "D":
                new_y += 25
                if world_data[new_y // 25][new_x // 25] == 1:
                    valid_move = False
            elif action == "L":
                new_x -= 25
                if world_data[new_y // 25][new_x // 25] == 1:
                    valid_move = False
            elif action == "R":
                new_x += 25
                if world_data[new_y // 25][new_x // 25] == 1:
                    valid_move = False

            # Reward and Q update
            reward, distance = get_reward(self, pacman, valid_move, self.prev_distance)
            self.prev_distance = distance
            next_state = get_state(self, pacman, tile_size)
            update_q(state, action, reward, next_state)

            # Move if valid
            if valid_move:
                self.rect.x = new_x
                self.rect.y = new_y

            self.direction = action

        else:
            px = self.rect.x
            py = self.rect.y
            directions = ['U', 'D', 'R', 'L']
            if self.rect.x == pacman.rect.x and self.rect.y == pacman.rect.y:
                save_q_table()
                running = False

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
            save_q_table()
            running = False


pacman = Pacman(25, 25, "R")

# tim = Ghost(225, 450, "D", 'media/redghost.png')
# pinky = Ghost(225, 250, "R", 'media/pinkghost.png')
matt = Ghost(450, 450, "L", 'media/cyanghost.png')
# clyde = Ghost(450, 250, "D", 'media/orangeghost.png')

matt.prev_distance = abs(matt.rect.x - pacman.rect.x) + abs(matt.rect.y - pacman.rect.y)

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
    
    # count = 0

    while running:
        
        # count += 1
        pygame.time.delay(10)
        screen.fill((0, 0, 0))
        world.draw()

        # tim.update()
        # pinky.update()
        matt.update()
        # clyde.update()
        pacman.update()

        for event in pygame.event.get():
            # escape
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == pygame.QUIT:
                running = False
        if len(world.dot_list) == 0:
            print("You Won!")
            running = False

        pygame.display.update()


        save_q_table()

    save_q_table()
    pygame.quit()

