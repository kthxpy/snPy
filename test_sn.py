from sn import isOccupied, getLvl, changeDir, move, genFood

def test_getLvl():
    levelData = {
                    "width"     : 4,
                    "height"    : 2,
                    "body"      : [(0, 0), (1, 0), (2, 0), (3,0), (3, 1), (2, 1), (1, 1)],
                    "food"      : [],
                }
    state = [["X","X","X","X"],[".","X","X","X"]]
    lvl = getLvl(levelData)
    assert lvl == state

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
    data = []
    data.append({
                    "width"  : 3,
                    "height" : 3,
                    "body"   : [(0, 0), (1, 0), (2, 0)],
                    "food"   : [],
                    "directions" : {
                                    "s" : (0, -1),
                                    "j" : (0,  1),
                                    "z" : (1, 0),
                                    "v" : (-1,  0),
                                    },
                    "direction" : "j",
                })
    states = [
                [(1, 0), (2, 0), (2, 1)],
            ]
    for i in range(len(data)):
        move(data[i])
        results.append(data[i]["body"] == states[i])
    assert results == [True]

def test_changeDir_invalid_direction():
    levelData = {
                    "directions" : {
                                    "s" : (0, -1),
                                    "j" : (0,  1),
                                    "z" : (1, 0),
                                    "v" : (-1,  0),
                                    },
                    "direction" : "j",
                }
    error = False
    try:
        changeDir(levelData, "f")
    except ValueError:
        error = True
    assert error == True

def test_changeDir_opossite_direction():
    levelData = {
                    "directions" : {
                                    "s" : (0, -1),
                                    "j" : (0,  1),
                                    "z" : (1, 0),
                                    "v" : (-1,  0),
                                    },
                    "direction" : "j",
                }

    changeDir(levelData, "s")
    assert levelData["direction"] == "j"

def test_changeDir_success():
    levelData = {
                    "directions" : {
                                    "s" : (0, -1),
                                    "j" : (0,  1),
                                    "z" : (1, 0),
                                    "v" : (-1,  0),
                                    },
                    "direction" : "j",
                }

    changeDir(levelData, "v")
    assert levelData["direction"] == "v"


def test_move_invalid_index():
    data = []
    data.append({
                    "width"     : 3,
                    "height"    : 3,
                    "body"      : [(0, 0), (1, 0), (2, 0)],
                    "direction" : "z",
                    "directions" : {
                                    "s" : (0, -1),
                                    "j" : (0,  1),
                                    "z" : (1, 0),
                                    "v" : (-1, 0),
                            }
                })

    data.append({
                    "width"     : 3,
                    "height"    : 3,
                    "body"      : [(2, 0), (1, 0), (0, 0)],
                    "direction" : "v",
                    "directions" : {
                                    "s" : (0, -1),
                                    "j" : (0,  1),
                                    "z" : (1, 0),
                                    "v" : (-1, 0),
                            }
                })
    errors = 0
    for levelData in data:
        try:
            move(levelData)
        except ValueError:
            errors += 1

    assert errors == 2


def test_genFood_all():
    levelData = {
                    "width"     : 5,
                    "height"    : 5,
                    "body"      : [(0, 0), (1, 0), (2, 0)],
                    "food"      : [],
                }
    genFood(levelData, 3)

    assert len(levelData["food"]) == 3

def test_genFood_not_enough_room():
    levelData = {
                    "width"     : 4,
                    "height"    : 2,
                    "body"      : [(0, 0), (1, 0), (2, 0), (3,0), (3, 1), (2, 1), (1, 1)],
                    "food"      : [],
                }
    genFood(levelData, 3)

    assert len(levelData["food"]) == 1
