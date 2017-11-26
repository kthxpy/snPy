from random import randrange

def drawLvl(levelData):
    width = levelData["width"]
    height = levelData["height"]
    level = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(".")
        level.append(row)

    for entity in levelData["body"]:
        x = entity[0]
        y = entity[1]
        level[y][x] = "X"

    for entity in levelData["food"]:
        x = entity[0]
        y = entity[1]
        level[y][x] = "?"

    for row in level:
        for character in row:
            print(character, " ", end="")
        print("")
    return

def isOccupied(listOfEntities, x, y):
    for entity in listOfEntities:
        if entity[0] == x and entity[1] == y:
            return True
    return False

def move(levelData, direction):
    width = levelData["width"]
    height = levelData["height"]
    sjvz = [(0,-1), (0,1), (-1, 0), (1, 0)]
    count = len(levelData["body"])
    last = levelData["body"][count -1]
    dir = ()

    if direction == "s":
        dir = sjvz[0]
    elif direction == "j":
        dir = sjvz[1]
    elif direction == "v":
        dir = sjvz[2]
    elif direction == "z":
        dir = sjvz[3]
    else:
        raise ValueError("This direction does not exist")

    entity = (last[0] + dir[0], last[1] + dir[1])

    if entity[0] < 0 or entity[1] >= width:
        raise ValueError("Game Over")
    elif entity[1] < 0 or entity[1] >= height:
        raise ValueError("Game Over")
    elif isOccupied(levelData["body"], entity[0], entity[1]):
        occupiedSpace = len(levelData["body"]) + len(levelData["food"])
        freePlace =  (occupiedSpace < levelSize)
        if not freePlace:
            raise ValueError("You Win!")
        else:
            raise ValueError("Game Over")
    else:
        levelData["body"].append(entity)
        if isOccupied(levelData["food"], entity[0], entity[1]):
            levelData["food"].pop(0)
        else:
            levelData["body"].pop(0)
    return

def genFood(levelData, amount):
    levelSize = levelData["width"] * levelData["height"]
    freePlace = len(levelData["body"]) + len(levelData["food"]) < levelSize

    while freePlace and amount > 0:
        randX = randrange(0, levelData["width"])
        randY = randrange(0, levelData["height"])
        f = (randX, randY)

        freeBody = not isOccupied(levelData["body"], randX, randY)
        freeFood = not isOccupied(levelData["food"], randX, randY)

        if freeBody and freeFood:
            levelData["food"].append((randX, randY))
            amount -= 1
    return


def run():
    end = False
    moves = 0
    fRefresh = 5
    fAmount = 1
    levelData = {
                    "width"  : 10,
                    "height" : 10,
                    "body" : [(0, 0), (1, 0), (2, 0)],
                    "food" : [(0,2)],
                }
    while not end:
        if moves > fRefresh:
            if levelData["food"]:
                for i in range(fAmount):
                    levelData["food"].pop(i)
            genFood(levelData, fAmount)
            moves = 0
            print("Moves reset to: ",  moves)
        drawLvl(levelData)
        dir = ""
        try:
            dir = input("Zadej smer pohybu")
        except RuntimeError:
            print("Unexpected Exception!")
        move(levelData, dir)
        moves += 1
        print("Moves added: ",  moves)
    return
