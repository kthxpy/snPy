from sn import isOccupied, move

def test_isOccupied_Positive():
    entities = [(0,0), (1,0), (2,0)]
    x, y = 1, 0
    result = isOccupied(entities, x, y)
    assert result == True

def test_isOccupied_Negative():
    entities = [(0,0), (1,0), (2,0)]
    x, y = 0, 1
    result = isOccupied(entities, x, y)
    assert result == False

def test_move_succes():
    entities = [(0,0), (1,0), (2,0)]
    results = []
    levelData = {
                    "width"     : 5,
                    "height"    : 5
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
        results.append(entities == states[i] )
    assert results == [True, True, True, True, True, True]

def test_move_invalid_direction():
    entities = [(0,0), (1,0), (2,0)]
    levelData = {
                    "width"     : 5,
                    "height"    : 5
                }
    error = False
    try:
        move(entities, levelData, "f")
    except ValueError:
        error = True
    assert error == True
