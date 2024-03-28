from unittest import TestCase
from javascript_task.MinMaxDiffer import min_max_differ



# import javascript_task
#
# class MinMaxDifferTest(TestCase):
#     def test_min_max_difference(self):
#
#         array_input = [2, 4, 5, 7, 8]
#         expected = [6]
#         self.assertEqual(expected, javascript_task.min_max_differ(array_input))
#

class MinMaxDifferTest(TestCase):
    def test_min_max_difference(self):
        array_input = [2, 4, 5, 7, 8]
        expected = [6]
        self.assertEqual(expected, min_max_differ(array_input))
