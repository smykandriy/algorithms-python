import unittest

from algo import get_minimum_sorting_range


class TestSortingRange(unittest.TestCase):
    def test_sorted_list(self):
        expected_result = (-1, -1)
        actual_result = get_minimum_sorting_range([x for x in range(10)])

        self.assertEqual(expected_result, actual_result)

    def test_unsorted_list(self):
        expected_result = (0, 9)
        actual_result = get_minimum_sorting_range([x for x in range(10, 0, -1)])

        self.assertEqual(expected_result, actual_result)

    def test_single_element_list(self):
        expected_result = (-1, -1)
        actual_result = get_minimum_sorting_range([1])

        self.assertEqual(expected_result, actual_result)
