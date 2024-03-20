import unittest

from OOP.cornflask.TaskOne import TaskOne


class TaskOneTest(unittest.TestCase):
    def test_collection_rate_less_than_50(self):
        myTaskOne = TaskOne()
        self.collection_rate = 60
        expected = 60 * 250 + 5000

        self.assertEqual(expected, myTaskOne.calculate_wages(self.collection_rate))


if __name__ == '__main__':
    unittest.main()
