images = {'X': 'wall.png', ' ': 'dot.png', }
world = []
BLOCK_SIZE = 32


def load(number):
    file = "level-%s.txt" % number
    for line in open(file):
        row = []
        for character in line:
            row.append(character)
        world.append(row)


def draw():
    for y, row in enumerate(world):
        for x, block in enumerate(row):
            image = images.get(block)
            if image:
                screen.blit(char_to_image[block], (x * BLOCK_SIZE, y * BLOCK_SIZE))


load(1)
print(world)
