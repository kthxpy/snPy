from sn import isOccupied, move

def test_isOccupied_Positive():
    listOfEntities = [(0,0), (1,0), (2,0)]
    x, y = 1, 0
    result = isOccupied(listOfEntities, x, y)
    assert result == True

def test_isOccupied_Negative():
    listOfEntities = [(0,0), (1,0), (2,0)]
    x, y = 0, 1
    result = isOccupied(listOfEntities, x, y)
    assert result == False

def test_move_succes():
    entities =  {
                    "body"  : [(0, 0), (1, 0), (2, 0)],
                    "food"  : [(2, 1)],
                }
    results = []
    levelData = {
                    "width"  : 5,
                    "height" : 5
                }
    directions = [ "j", "j", "z", "z", "s", "v"]
    states = [
                [(1,0), (2,0), (2,1)],
                [(2,0), (2,1), (2,2)],
                [(2,1), (2,2), (3,2)],
                [(2,2), (3,2), (4,2)],
                [(3,2), (4,2), (4,1)],
                [(4,2), (4,1), (3,1)]
             ]
    for i in range(len(states)):
        move(entities, levelData, directions[i])
        results.append(entities["body"] == states[i] )
    assert results == [True, True, True, True, True, True]

def test_move_invalid_direction():
    entities =  {
                    "body"  : [(0, 0), (1, 0), (2, 0)],
                    "food"  : [(2, 1)],
                }
    levelData = {
                    "width"     : 5,
                    "height"    : 5,
                }
    error = False
    try:
        move(entities, levelData, "f")
    except ValueError:
        error = True
    assert error == True
