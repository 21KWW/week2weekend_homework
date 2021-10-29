import unittest
from classes.Room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        playlist1 = ["Rockferry"]
        playlist2 = ["Voodoo Child"]
        guests1 = ["Meg"]
        guests2 = ["James"]
        self.room1 = Room("Chill Room", 20, 5, playlist1, guests1)
        self.room2 = Room("Blue Room", 10, 10, playlist2, guests2)

    def test_room_has_name(self):
        self.assertEqual("Chill Room", self.room1.name)
        self.assertEqual("Blue Room", self.room2.name)

    def test_room_has_capacity(self):
        self.assertEqual(20, self.room1.capacity)
        self.assertEqual(10, self.room2.capacity)

    def test_room_has_entryfee(self):
        self.assertEqual(5, self.room1.entryfee)
        self.assertEqual(10, self.room2.entryfee)

    def test_room_has_playlist(self):
        self.assertIsNotNone(len(self.room1.playlist))
        self.assertIsNotNone(len(self.room2.playlist))

    def test_room_has_guests(self):
        self.assertIsNotNone(len(self.room1.guests))
        self.assertIsNotNone(len(self.room2.guests))