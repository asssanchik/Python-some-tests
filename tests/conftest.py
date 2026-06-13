import pytest



def _calculate(a, b):
    return a + b



@pytest.fixture
def calculator():
    return _calculate