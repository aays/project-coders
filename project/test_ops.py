import pytest
from project import ops

def test_add_fun():
    assert ops.add_fun(1, 2) == 3
    with pytest.raises(AssertionError, match 'wrong type!')
        ops.add_fun(1, '2')
