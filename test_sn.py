from sn import isOccupied, move, genFood

def test_isOccupied_Positive():
    listOfEntities = [(0, 0), (1, 0), (2, 0)]
    x, y = 1, 0
    result = isOccupied(listOfEntities, x, y)
    assert result == True

def test_isOccupied_Negative():
    listOfEntities = [(0, 0), (1, 0), (2, 0)]
    x, y = 0, 1
    result = isOccupied(listOfEntities, x, y)
    assert result == False

def test_move_succes():
    results = []
    levelData = {
                    "width"  : 5,
                    "height" : 5,
                    "body"   : [(0, 0), (1, 0), (2, 0)],
                    "food"   : [],
                }
    directions = ["j", "j", "z", "z", "s", "v"]
    states = [
        [(1, 0), (2, 0), (2, 1)],
        [(2, 0), (2, 1), (2, 2)],
        [(2, 1), (2, 2), (3, 2)],
        [(2, 2), (3, 2), (4, 2)],
        [(3, 2), (4, 2), (4, 1)],
        [(4, 2), (4, 1), (3, 1)]
    ]
    for i in range(len(states)):
        move(levelData, directions[i])
        results.append(levelData["body"] == states[i] )
    assert results == [True, True, True, True, True, True]

def test_move_invalid_direction():
    levelData = {
                    "width"     : 5,
                    "height"    : 5,
                    "body"  : [(0, 0), (1, 0), (2, 0)],
                    "food"  : [(2, 1)],
                }
    error = False
    try:
        move(levelData, "f")
    except ValueError:
        error = True
    assert error == True

def test_genFood_all():
    levelData = {
                    "width"     : 5,
                    "height"    : 5,
                    "body"  : [(0, 0), (1, 0), (2, 0)],
                    "food"  : [],
                }
    genFood(levelData, 3)

    assert len(levelData["food"]) == 3

def test_genFood_not_enough_room():
    levelData = {
                    "width"     : 4,
                    "height"    : 2,
                    "body"  : [(0, 0), (1, 0), (2, 0), (3,0), (3, 1), (2, 1), (1, 1)],
                    "food"  : [],
                }
    genFood(levelData, 3)

    assert len(levelData["food"]) == 1
