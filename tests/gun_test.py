import unittest
from OOP.guns.gun import Gun


class TestGun(unittest.TestCase):

    def test_load_ammunition(self):
        self.gun = Gun("9mm", "Pistol")
        self.assertEqual(self.gun.load_ammunition(10), 10)
        self.assertEqual(self.gun.load_ammunition(5), 15)
        self.assertEqual(self.gun.load_ammunition(10), 25)

    def test_fire_with_ammunition(self):
        self.gun = Gun("9mm", "Pistol")
        self.gun.load_ammunition(10)
        self.assertEqual(self.gun.fire(), 9)

    def test_fire_without_ammunition(self):
        self.gun = Gun("9mm", "Pistol")
        self.assertEqual(self.gun.fire(), 0)
