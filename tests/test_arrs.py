import pytest
from arrs import get, my_slice

def test_get_existing_index():
    array = [1, 2, 3, 4, 5]
    assert get(array, 2) == 3

def test_get_nonexisting_index_with_default():
    array = [1, 2, 3, 4, 5]
    assert get(array, 10, "default") == "default"

def test_get_nonexisting_index_without_default():
    array = [1, 2, 3, 4, 5]
    assert get(array, 10) == None

def test_my_slice_no_arguments():
    array = [1, 2, 3, 4, 5]
    assert my_slice(array) == [1, 2, 3, 4, 5]

def test_my_slice_with_start():
    array = [1, 2, 3, 4, 5]
    assert my_slice(array, 2) == [3, 4, 5]

def test_my_slice_with_end():
    array = [1, 2, 3, 4, 5]
    assert my_slice(array, end=3) == [1, 2, 3]

def test_my_slice_with_start_and_end():
    array = [1, 2, 3, 4, 5]
    assert my_slice(array, 1, 4) == [2, 3, 4]
