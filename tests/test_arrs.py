import pytest
from arrs import get, my_slice
def test_get_negative_index():
    array = [1, 2, 3, 4, 5]
    assert get(array, -1) == None

def test_get_noninteger_index():
    array = [1, 2, 3, 4, 5]
    with pytest.raises(TypeError):
        get(array, 2.5)

def test_my_slice_negative_start():
    array = [1, 2, 3, 4, 5]
    assert my_slice(array, -2) == [4, 5]

def test_my_slice_negative_end():
    array = [1, 2, 3, 4, 5]
    assert my_slice(array, end=-2) == [1, 2, 3]

def test_my_slice_start_and_end_out_of_bounds():
    array = [1, 2, 3, 4, 5]
    assert my_slice(array, -10, 10) == [1, 2, 3, 4, 5]

def test_my_slice_non_list_or_tuple_argument():
    with pytest.raises(TypeError):
        my_slice("not_an_iterable")

def test_get_non_list_argument():
    with pytest.raises(TypeError):
        get("not_an_iterable", 2)
