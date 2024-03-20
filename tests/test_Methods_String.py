from unittest import TestCase

from OOP.cornflask.Methods_String import MethodString


class test_MethodString(TestCase):
    def test_for_name(self):
        myMethodString = MethodString()
        myMethodString.name_inputs("timi")
        self.assertEqual("TIMI", myMethodString.printString())
