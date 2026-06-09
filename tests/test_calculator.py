import pytest

from src.main import Calculator


@pytest.mark.parametrize(
    "x, y, res",
    [
        (1, 2, 0.5),
        (5, -1, -5)
    ]
)
def test_divide():
    x = 1
    y = 2
    res = 0.5
    assert Calculator().divide(x, y) == res