import unittest
from msd_sort_basic import MSDSortBasic
import random
import string

class TestMSDSortBasic(unittest.TestCase):
    def setUp(self):
        self.sorter = MSDSortBasic()
    
    def test_empty_array(self):
        arr = []
        self.sorter.sort_by_position(arr, 0)
        self.assertEqual(arr, [])
        self.assertTrue(self.sorter.is_sorted_by_position(arr, 0))
    
    def test_single_element(self):
        arr = ["a"]
        self.sorter.sort_by_position(arr, 0)
        self.assertEqual(arr, ["a"])
        self.assertTrue(self.sorter.is_sorted_by_position(arr, 0))
    
    def test_sort_by_first_char(self):
        arr = ["dog", "cat", "bird", "ant", "elephant"]
        self.sorter.sort_by_position(arr, 0)
        # After sorting by first character: ant, bird, cat, dog, elephant
        for i in range(1, len(arr)):
            self.assertLessEqual(self._first_char(arr[i-1]), self._first_char(arr[i]))
        self.assertTrue(self.sorter.is_sorted_by_position(arr, 0))
    
    def test_sort_by_second_char(self):
        arr = ["ba", "bc", "aa", "ac", "bb", "ab"]
        self.sorter.sort_by_position(arr, 1)
        # After sorting by second character, order is determined by the second letter only
        for i in range(1, len(arr)):
            self.assertLessEqual(self._char_at(arr[i-1], 1), self._char_at(arr[i], 1))
        self.assertTrue(self.sorter.is_sorted_by_position(arr, 1))
    
    def test_sort_with_some_strings_too_short(self):
        arr = ["ab", "a", "abc", "abcd", ""]
        self.sorter.sort_by_position(arr, 1)
        self.assertTrue(self.sorter.is_sorted_by_position(arr, 1))
        for i in range(len(arr)):
            if i > 0 and self._char_at(arr[i-1], 1) != -1:
                self.assertNotEqual(self._char_at(arr[i], 1), -1)
    
    def test_stability_on_equal_keys(self):
        # Test that strings with the same key (character at position d) maintain their relative order
        arr = ["cat", "cab", "car"]
        original_order = arr.copy()
        self.sorter.sort_by_position(arr, 0)
        self.assertEqual(arr, original_order)
    
    def test_large_random_array(self):
        random.seed(42)
        arr = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(1000)]
        position = 2  # Sort by the third character
        self.sorter.sort_by_position(arr, position)
        self.assertTrue(self.sorter.is_sorted_by_position(arr, position))
    
    def test_special_characters(self):
        arr = ["a!", "a@", "a#", "a$", "a%"]
        self.sorter.sort_by_position(arr, 1)
        self.assertTrue(self.sorter.is_sorted_by_position(arr, 1))
    
    def _first_char(self, s):
        return self._char_at(s, 0)
    
    def _char_at(self, s, d):
        if d < len(s):
            return ord(s[d])
        return -1

if __name__ == '__main__':
    unittest.main()
