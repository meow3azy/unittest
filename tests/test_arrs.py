import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

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

