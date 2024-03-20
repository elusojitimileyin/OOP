import unittest

from OOP.segentDisplay.sevensegmentdisplay import SevenSegmentDisplay


class SevenSegmentDisplayTest(unittest.TestCase):
    def test_print_Segments(self):
        mySevenSegmentDisplay = SevenSegmentDisplay()
        self.assertEqual("11111111", mySevenSegmentDisplay.print_number("11111111"))
