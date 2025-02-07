import pygame
import random

class Grain:
    solids = ("Sand", "Grass", "Stone")
    def __init__(self, size, xPos, yPos):
        self.size = size
        self.xPos = xPos
        self.yPos = yPos
        self.updated = False

        self.surf = pygame.surface.Surface((self.size, self.size))
        self.rect = self.surf.get_rect(topleft=(self.xPos, self.yPos))
        

    #Draw to the Screen
    def update(self, screen):
        self.surf.fill(self.color)
        screen.blit(self.surf, self.rect)

    #Swap two 
    def exchange(self, other):
        newSelf = other.__class__(self.size, self.xPos, self.yPos)        
        newOther = self.__class__(other.size, other.xPos, other.yPos)
        newSelf.updated = True
        newOther.updated = True
        return newSelf, newOther

class Empty(Grain):
    def __init__(self, size, xPos, yPos):
        super().__init__(size, xPos, yPos)
        self.type = "Empty"
        self.color = [0, 0, 0]    

class Sand(Grain):
    def __init__(self, size, xPos, yPos):
        super().__init__(size, xPos, yPos)
        self.type = "Sand"
        self.color = [198, 174, 128]

    def move(self, grid, row, col):
            if self.updated:
                self.updated = False
                return
            self.updated = True

            #FALL DOWN
            if row < len(grid)-1:
                if grid[row+1][col].type in ("Empty", "Water"):
                    grid[row][col], grid[row+1][col] = grid[row][col].exchange(grid[row+1][col])
                    

            #FALL LEFT OR RIGHT
            if col < len(grid[0])-1 and col > 1 and row < len(grid)-1:
                if grid[row+1][col].type in solids and grid[row+1][col-1].type in ("Empty", "Water") and grid[row+1][col+1].type in ("Empty", "Water"):
                    direction = random.choice((-1, 1))
                    grid[row][col], grid[row+1][col+direction] = grid[row][col].exchange(grid[row+1][col+direction])
        
            #FALL LEFT
            if col > 0 and row < len(grid)-1:
                if grid[row+1][col].type in solids and grid[row+1][col-1].type in ("Empty", "Water"):
                    grid[row][col], grid[row+1][col-1] = grid[row][col].exchange(grid[row+1][col-1])

            #FALL RIGHT
            if col < len(grid[0])-1 and row < len(grid)-1:
                if grid[row+1][col].type in solids and grid[row+1][col+1].type in ("Empty", "Water"):
                    grid[row][col], grid[row+1][col+1] = grid[row][col].exchange(grid[row+1][col+1])

class Grass(Grain):
    def __init__(self, size, xPos, yPos):
        super().__init__(size, xPos, yPos)
        self.type = "Grass"
        self.color = "#66a64e"

    def move(self, grid, row, col):
        if self.updated:
            self.updated = False
            return
        self.updated = True



        #FALL DOWN
        if row < len(grid)-1:
            if grid[row+1][col].type in ("Empty", "Water"):
                grid[row][col], grid[row+1][col] = grid[row][col].exchange(grid[row+1][col])

        #FALL LEFT OR RIGHT
        if col < len(grid[0])-1 and col > 1 and row < len(grid)-1:
            if grid[row+1][col].type in solids and grid[row+1][col-1].type in ("Empty", "Water") and grid[row+1][col+1].type in ("Empty", "Water"):
                direction = random.choice((-1, 1))
                grid[row][col], grid[row+1][col+direction] = grid[row][col].exchange(grid[row+1][col+direction])
        
        #FALL LEFT
        if col > 0 and row < len(grid)-1:
            if grid[row+1][col].type in solids and grid[row+1][col-1].type in ("Empty", "Water"):
                grid[row][col], grid[row+1][col-1] = grid[row][col].exchange(grid[row+1][col-1])

        #FALL RIGHT
        if col < len(grid[0])-1 and row < len(grid)-1:
            if grid[row+1][col].type in solids and grid[row+1][col+1].type in ("Empty", "Water"):
                grid[row][col], grid[row+1][col+1] = grid[row][col].exchange(grid[row+1][col+1])

class Water(Grain):
    def __init__(self, size, xPos, yPos):
        super().__init__(size, xPos, yPos)
        self.type = "Water"
        self.color = "#67b3be"

    def move(self, grid, row, col):
        if self.updated:
            self.updated = False
            return
        self.updated = True
        
        #FALL DOWN
        if row < len(grid)-1:
            if grid[row+1][col].type == "Empty":
                grid[row][col], grid[row+1][col] = grid[row][col].exchange(grid[row+1][col])

        #FALL LEFT OR RIGHT
        if col < len(grid[0])-1 and col > 1 and row < len(grid)-1:
            if grid[row+1][col].type in ("Sand", "Grass", "Water", "Stone") and grid[row][col-1].type not in ("Sand", "Grass", "Water", "Stone") and grid[row+1][col+1].type not in ("Sand", "Grass", "Water", "Stone") and grid[row+1][col-1].type == "Empty" and grid[row+1][col+1].type == "Empty":
                direction = random.choice((-1, 1))
                grid[row][col], grid[row+1][col+direction] = grid[row][col].exchange(grid[row+1][col+direction])
        
        #FALL LEFT
        if col > 0 and row < len(grid)-1:
            if grid[row+1][col].type in ("Sand", "Grass", "Water", "Stone") and grid[row][col-1].type not in ("Sand", "Grass", "Water", "Stone") and grid[row+1][col-1].type == "Empty":
                grid[row][col], grid[row+1][col-1] = grid[row][col].exchange(grid[row+1][col-1])

        #FALL RIGHT
        if col < len(grid[0])-1 and row < len(grid)-1:
            if grid[row+1][col].type in ("Sand", "Grass", "Water", "Stone") and grid[row][col+1].type not in ("Sand", "Grass", "Water", "Stone") and grid[row+1][col+1].type == "Empty":
                grid[row][col], grid[row+1][col+1] = grid[row][col].exchange(grid[row+1][col+1])

        #FLOW RIGHT
        if col < len(grid[0])-1:
            if grid[row][col+1].type == "Empty": 
                grid[row][col], grid[row][col+1] = grid[row][col].exchange(grid[row][col+1])

        #FLOW LEFT
        if col > 1:
            if grid[row][col-1].type == "Empty": 
                grid[row][col], grid[row][col-1] = grid[row][col].exchange(grid[row][col-1])

class Stone(Grain):
    def __init__(self, size, xPos, yPos):
        super().__init__(size, xPos, yPos)
        self.type = "Stone"
        self.color = "#5c5c5c"

class NPC(Grain):
    def __init__(self, size, xPos, yPos):
        super().__init__(size, xPos, yPos)
        self.type = "NPC"
        self.color = "#883333"
        self.health = 100

        self.moveChance = 10
        self.cdc = 10
        self.dir = 1

    def move(self, grid, row, col):
        if self.updated:
            self.updated = False
            return
        self.updated = True

        #DIE
        if row > 0:
            if grid[row-1][col].type not in ("Empty", "Water", "Stone") or self.health == 0:
                grid[row][col] = Empty(self.size, self.xPos, self.yPos)

        #FALL DOWN
        if row < len(grid)-1:
            if grid[row+1][col].type == "Empty":
                grid[row][col], grid[row+1][col] = grid[row][col].exchange(grid[row+1][col])

        #FLOAT
        if row > 0:
            if grid[row-1][col].type == "Water":
                grid[row][col], grid[row-1][col] = grid[row][col].exchange(grid[row-1][col])


        #Randomly choose to move left or right
        self.dir *= random.choice((-1, 1))

        #Move at a chance
        if random.choice(range(self.moveChance)) == 0:

            #Move Left or Right
            if col > 0 and col < len(grid[0])-1:
                if grid[row][col+self.dir].type == "Empty":
                    grid[row][col], grid[row][col+self.dir] = grid[row][col].exchange(grid[row][col+self.dir])

            #Move Up Left or Up Right
            if col > 0 and col < len(grid[0])-1 and row > 0:
                if grid[row][col+self.dir].type in ("Sand", "Grass", "Stone","Water") and grid[row-1][col+self.dir].type == "Empty":
                    grid[row][col], grid[row-1][col+self.dir] = grid[row][col].exchange(grid[row-1][col+self.dir])

class Void(Grain):
    def __init__(self, size, xPos, yPos):
        super().__init__(size, xPos, yPos)
        self.type = "Void"
        self.color = "#36013f"

    def move(self, grid, row, col):
        grid[row-1][col] = Empty(grid[row-1][col].size, grid[row-1][col].xPos, grid[row-1][col].yPos) #Top
        grid[row+1][col] = Empty(grid[row+1][col].size, grid[row+1][col].xPos, grid[row+1][col].yPos) #Bottom
        grid[row][col-1] = Empty(grid[row][col-1].size, grid[row][col-1].xPos, grid[row][col-1].yPos) #Left
        grid[row][col+1] = Empty(grid[row][col+1].size, grid[row][col+1].xPos, grid[row][col+1].yPos) #Right
        grid[row-1][col-1] = Empty(grid[row-1][col-1].size, grid[row-1][col-1].xPos, grid[row-1][col-1].yPos) #Top Left
        grid[row-1][col+1] = Empty(grid[row-1][col+1].size, grid[row-1][col+1].xPos, grid[row-1][col+1].yPos) #Top Right
        grid[row+1][col-1] = Empty(grid[row+1][col-1].size, grid[row+1][col-1].xPos, grid[row+1][col-1].yPos) #Bottom Left
        grid[row+1][col+1] = Empty(grid[row+1][col+1].size, grid[row+1][col+1].xPos, grid[row+1][col+1].yPos)





pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

grainSize = 10
currentType = "Sand"

solids = ("Sand", "Grass")
liquids = ("Water", "Empty", "Cloud")

grid = [[Empty(grainSize, x*grainSize, y*grainSize) for x in range(screen.get_width()//grainSize)] for y in range(screen.get_height()//grainSize)]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SystemExit()
            quit()

        if event.type == pygame.KEYDOWN:

            #CLEAR GRID
            if event.key == pygame.K_SPACE:
                for row in range(len(grid)):
                    for col in range(len(grid[row])):
                        grid[row][col] = Empty(grainSize, grid[row][col].xPos, grid[row][col].yPos)
                        
            #Set to different modes
            if event.key == pygame.K_w:
                currentType = "Water"
            elif event.key == pygame.K_s:
                currentType = "Sand"
            elif event.key == pygame.K_e:
                currentType = "Empty"
            elif event.key == pygame.K_g:
                currentType = "Grass"
            elif event.key == pygame.K_r:
                currentType = "Stone"
            elif event.key == pygame.K_n:
                currentType = "NPC"
            elif event.key == pygame.K_v:
                currentType = "Void"
            print(currentType)

        if currentType == "NPC":
            if event.type == pygame.MOUSEBUTTONDOWN:
                locX, locY = pygame.mouse.get_pos()[0]//grainSize, pygame.mouse.get_pos()[1]//grainSize
                grid[locY][locX] = NPC(grainSize, grid[locY][locX].xPos, grid[locY][locX].yPos)


    #Click to color in the squares
    if pygame.mouse.get_pressed()[0]:

        #Grid locations of where you clicked
        locX, locY = pygame.mouse.get_pos()[0]//grainSize, pygame.mouse.get_pos()[1]//grainSize

        #Click to set that grid square to the current grain type
        if 1 < locX < len(grid[0])-2:
            if currentType == "Empty":
                grid[locY][locX] = Empty(grainSize, grid[locY][locX].xPos, grid[locY][locX].yPos)
            elif currentType == "Sand":
                grid[locY][locX] = Sand(grainSize, grid[locY][locX].xPos, grid[locY][locX].yPos)
            elif currentType == "Water":
                grid[locY][locX] = Water(grainSize, grid[locY][locX].xPos, grid[locY][locX].yPos)
            elif currentType == "Stone":
                grid[locY][locX] = Stone(grainSize, grid[locY][locX].xPos, grid[locY][locX].yPos)
            elif currentType == "Grass":
                grid[locY][locX] = Grass(grainSize, grid[locY][locX].xPos, grid[locY][locX].yPos)
            elif currentType == "Void":
                grid[locY][locX] = Void(grainSize, grid[locY][locX].xPos, grid[locY][locX].yPos)
    

    #Iterate through all squares
    # Iterate through all squares from bottom to top
    for row in range(len(grid) - 1, -1, -1):
        for col in range(len(grid[row])):

            this = grid[row][col]

            if this.type not in ("Empty", "Stone"):
                grid[row][col].move(grid, row, col)



            this.update(screen)
            #screen.blit(font.render(this.type[0], False, "White"), (this.xPos, this.yPos))

            

    pygame.display.update()

    clock.tick(60)