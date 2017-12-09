import os
from random import randrange
from msvcrt import getch, kbhit

### CONSOLE SPECIFIC FUNCTIONS ###

def drawLvl(levelData):
    width = levelData["width"]
    height = levelData["height"]
    level = []
    levelStr = ""
    xOff = 20
    yOff = 10

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

    print(yOff * "\n", end="")
    for row in level:
        print(xOff * " ",  end="")
        for character in row:
            print(character, " ", end="")
        print("")
    return

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def keyDown():
    while True:
        ch = ord(getch())
        if ch == 0 or ch == 224:
            ch = ord(getch())
        return ch

def onKeyDown(levelData, key):

    if key == levelData["keys"]["left"]:
        levelData["direction"] = "v"
    elif key == levelData["keys"]["up"]:
        levelData["direction"] = "s"
    elif key == levelData["keys"]["right"]:
        levelData["direction"] = "z"
    elif key == levelData["keys"]["down"]:
        levelData["direction"] = "j"
    return

def onLevelChange(levelData):
    clear()
    drawLvl(levelData)
    return


### GAMELOGIC FUNCTIONS ###

def isOccupied(listOfEntities, x, y):
    for entity in listOfEntities:
        if entity[0] == x and entity[1] == y:
            return True
    return False

def changeDir(levelData, direction):
    if direction not in levelData["directions"]:
        raise ValueError("This direction does not exist")
    else:
        oldOff = levelData["directions"][levelData["direction"]]
        newOff = levelData["directions"][direction]
        print(oldOff, newOff)
        offSum = abs(oldOff[0] + newOff[0]) + abs(oldOff[1] + newOff[1])
        # Check for opposite directions (do not want to use them)
        if offSum > 0:
            levelData["direction"] = direction
    return

def move(levelData):
    width = levelData["width"]
    height = levelData["height"]
    count = len(levelData["body"])
    last = levelData["body"][count -1]
    d = levelData["direction"]
    offset = levelData["directions"][d]

    entity = (last[0] + offset[0], last[1] + offset[1])

    if  not (0 <= entity[0] < width  and 0 <= entity[1] < height):
        print("Entity out of bounds: ", entity)
        raise ValueError("Game Over")
    elif isOccupied(levelData["body"], entity[0], entity[1]):
        print("Position occupied: ", entity)
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
    onLevelChange(levelData)
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
    levelData = {
                    "width"     : 10,
                    "height"    : 10,
                    "body"      : [(0, 0), (1, 0), (2, 0)],
                    "food"      : [(0,2)],
                    "direction" : "z",
                    "moves"     : 0,
                    "fRefresh"  : 30,
                    "fAmount"   : 1,
                    "keys"      : {
                                    "esc" : 27, "enter" : 13, "left" : 75,
                                    "up": 72, "right": 77, "down": 80,
                                    },
                    "fLimit"    : 15000,
                    "fTicks"    : 0,
                    "directions" : {
                                    "s" : (0, -1),
                                    "j" : (0,  1),
                                    "z" : (1, 0),
                                    "v" : (-1,  0),
                            }
                }

    while not end:
        if kbhit():
            k = keyDown()
            onKeyDown(levelData, k)
        lvlTick(levelData)
        if levelData["fTicks"] > levelData["fLimit"]:
            move(levelData)
            levelData["moves"] += 1
            levelData["fTicks"] = 0
            onLevelChange(levelData)
        levelData["fTicks"] +=1
    return

run()
