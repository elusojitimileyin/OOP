import unittest

from OOP.javascript_task.javascript_task import output_total_occurring_number_short


class Output_test(unittest.TestCase):

    def test_output_total_occurring_number_short(self):
        input_list = [1, 2, 2, 3, 4, 2, 4, 4, 4]
        expected_output = [4, 4]
        self.assertEqual(expected_output, output_total_occurring_number_short(input_list))
