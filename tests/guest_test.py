import unittest
from classes.Guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("James", 100, "Rockferry")
        self.guest2 = Guest("Meg", 50, "Don't Stop Me Now")

    def test_guest_has_name(self):
        self.assertEqual("James", self.guest1.name)
        self.assertEqual("Meg", self.guest2.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest1.wallet)
        self.assertEqual(50, self.guest2.wallet)

    def test_guest_has_favsong(self):
        self.assertEqual("Rockferry", self.guest1.favsong)
        self.assertEqual("Don't Stop Me Now", self.guest2.favsong)
