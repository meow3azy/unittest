<<<<<<< HEAD
import unittest
from utils import arrs, my_slice
=======
import pytest
from arrs import get, my_slice
>>>>>>> develop

def test_get_existing_index():
    array = [1, 2, 3, 4, 5]
    assert get(array, 2) == 3

def test_get_nonexisting_index_with_default():
    array = [1, 2, 3, 4, 5]
    assert get(array, 10, "default") == "default"

<<<<<<< HEAD
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_get_negative_index(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), 3)
        self.assertEqual(arrs.get([1, 2, 3], -4, "test"), "test")

    def test_my_slice_negative_indices(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -3, -1), [3, 4])

class TestArraySlice(unittest.TestCase):
    def test_slice_with_positive_indices(self):
        coll = [1, 2, 3, 4, 5]
        result = my_slice(coll, 1, 4)
        self.assertEqual(result, [2, 3, 4])

    def test_slice_with_negative_indices(self):
        coll = [1, 2, 3, 4, 5]
        result = my_slice(coll, -3, -1)
        self.assertEqual(result, [3, 4])

    def test_slice_with_start_none(self):
        coll = [1, 2, 3, 4, 5]
        result = my_slice(coll, None, 3)
        self.assertEqual(result, [1, 2, 3])

    def test_slice_with_end_none(self):
        coll = [1, 2, 3, 4, 5]
        result = my_slice(coll, 2, None)
        self.assertEqual(result, [3, 4, 5])

    def test_slice_with_start_and_end_none(self):
        coll = [1, 2, 3, 4, 5]
        result = my_slice(coll)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_slice_with_empty_coll(self):
        coll = []
        result = my_slice(coll)
        self.assertEqual(result, [])
=======
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
>>>>>>> develop
