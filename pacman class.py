class pacman(object):
    def __init__(self,direction,x,y):
        self.direction = direction
        self.x = x
        self.y = y


    def move(self):
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_DOWN:
        #         self.direction = "d"
        #     if event.key == pygame.K_LEFT:
        #         self.direction = "l"
        #     if event.key == pygame.K_RIGHT:
        #         self.direction = "r"
        #     if event.key == pygame.K_UP:
        #         self.direction = "u"

        match self.direction:
            case "u":
                self.x -= 1
            case "d":
                self.x += 1
            case "r":
                self.y += 1
            case "l":
                self.y -= 1
        print(self.direction)
        print(self.x)
        print(self.y)

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)