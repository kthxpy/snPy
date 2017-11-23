def drawLvl(entities):
    width = 5
    height = 5
    level = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(".")
        level.append(row)

    for entity in entities:
        x = entity[0]
        y = entity[1]
        level[y][x] = "X"

    for row in level:
        for character in row:
            print(character, " ", end="")
        print("")
    return

def isOccupied(entities, x, y):
    for entity in entities:
        if entity[0] == x and entity[1] == y:
            return True
    return False

def move(entities, direction):
    width = 5
    height = 5
    sjvz = [(0,-1), (0,1), (-1, 0), (1, 0)]
    last = entities[len(entities)-1]
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
        entities.append(entity)
        entities.pop(0)
    return 

def run():
    entities = [(0,0)]

    drawLvl(entities)
    dir = ""
    
    try:
        dir = input("Zadej smer pohybu")
    except RuntimeError:
        print("Unexpected Exception!")

    move(entities, dir)
    return

