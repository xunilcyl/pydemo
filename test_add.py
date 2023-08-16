
from add import add

def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(9999, 1) == 10000
    assert add(100000, 100000) == 200000
