from app import add  # type: ignore

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0