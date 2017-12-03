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

    if  not (0 < entity[0] < width  or 0 < entity[1] < height):
        raise ValueError("Game Over")
    elif isOccupied(levelData["body"], entity[0], entity[1]):
        raise ValueError("Game Over")
    elif isOccupied(levelData["food"], entity[0], entity[1]):
        levelData["body"].append(entity)
        levelData["food"].pop(0)
    else:
        levelData["body"].append(entity)
        levelData["body"].pop(0)
    return

def freeSpace(levelData):
    levelSize = levelData["width"] * levelData["height"]
    occupiedSpace = len(levelData["body"]) + len(levelData["food"])
    free = levelSize - occupiedSpace
    return free

def genFood(levelData, amount):

    while freeSpace(levelData) and amount:
        randX = randrange(0, levelData["width"])
        randY = randrange(0, levelData["height"])

        bite = (randX, randY)

        if bite not in levelData["body"] and bite not in levelData["food"]:
            levelData["food"].append(bite)
            amount -= 1
    return

def lvlTick(levelData):
    if levelData["moves"] > levelData["fRefresh"]:
            if levelData["food"]:
                for i in range(levelData["fAmount"]):
                    levelData["food"].pop(i)
            genFood(levelData, levelData["fAmount"])
            levelData["moves"] = 0
    return

def run():
    end = False
    moves = 0
    fRefresh = 5
    fAmount = 1
    levelData = {
                    "width"     : 10,
                    "height"    : 10,
                    "body"      : [(0, 0), (1, 0), (2, 0)],
                    "food"      : [(0,2)],
                    "direction" : "z",
                    "moves"     : 0,
                    "fRefresh"  : 5,
                    "fAmount"   : 1,
                }
    while not end:
        lvlTick(levelData)
        drawLvl(levelData)
        dir = ""
        try:
            dir = input("Zadej smer pohybu")
        except RuntimeError:
            print("Unexpected Exception!")
        move(levelData, dir)
        levelData["moves"] += 1
        levelData["direction"] = dir
    return

run()
