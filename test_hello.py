#from hello import add

#def test_add():
#    assert add(1,2) == 3

import pytest
from hello import add

# Aquí se parametriza la prueba para probar varios casos
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),  # Caso de prueba 1
    (4, 5, 9),  # Caso de prueba 2
    (-1, 1, 0), # Caso de prueba 3
    (0, 0, 0),  # Caso de prueba 4
])
def test_add(a, b, expected):
    assert add(a, b) == expected
