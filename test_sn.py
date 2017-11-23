from sn import isOccupied

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

def test_move_invalid_direction():
    entities = [(0,0), (1,0)]

    error = False
    try:
        move(entities, "f")
    except ValueError:
        error = True
    assert error == True 
