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

def move(entities, direction):
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
        print("Invalid move")

    entity = (last[0] + dir[0], last[1] + dir[1])
    entities.append(entity)
    entities.pop(0)
    
    return entities

entities = [(0,0), (1,0)]
drawLvl(entities)
entities = move(entities, "z")
drawLvl(entities)
entities = move(entities, "j")
drawLvl(entities)