import unittest
import group

class MyTestCase(unittest.TestCase):
    def test_groups_of_3_1(self):
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        actual = group.groups_of_3([1,2,3,4,5,6,7,8,9])
        self.assertEqual(expected, actual)
    def test_groups_of_3(self):
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        actual = group.groups_of_3([1,2,3,4,5,6,7,8])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
