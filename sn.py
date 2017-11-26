def drawLvl(entities, levelData):
    width = levelData["width"]
    height = levelData["height"]
    level = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(".")
        level.append(row)

    for entity in entities["body"]:
        x = entity[0]
        y = entity[1]
        level[y][x] = "X"

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

def move(entities, levelData, direction):
    width = levelData["width"]
    height = levelData["height"]
    sjvz = [(0,-1), (0,1), (-1, 0), (1, 0)]
    count = len(entities["body"])
    last = entities["body"][count -1]
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
    elif isOccupied(entities, entity[0], entity[1]):
        raise ValueError("Game Over")
    else:
        entities["body"].append(entity)
        entities["body"].pop(0)
    return

def run():
    end = False
    entities =  {
                    "body" : [(0, 0), (1, 0), (2, 0)],
                    "food" : [2, 1],
                }
    levelData = {
                    "width"  : 10,
                    "height" : 10,
                }
    while not end:
        drawLvl(entities)
        dir = ""
        try:
            dir = input("Zadej smer pohybu")
        except RuntimeError:
            print("Unexpected Exception!")
        move(entities, levelData, dir)
        print(entities)
    return

#run()
