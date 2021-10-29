import unittest
from classes.Room import Room
from classes.Guest import Guest
from classes.Song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        song1 = Song("Rockferry", "Duffy", "")
        song2 = Song("Warwick Avenue", "Duffy", "")
        song3 = Song("Serious", "Duffy", "")
        song4 = Song("Fever", "Kylie Minogue", "")
        song5 = Song("Love At First Sight", "Kylie Minogue", "")
        song6 = Song("Can't Get You Out Of My Head", "Kylie Minogue", "")
        song7 = Song("Love And Kisses", "Danni Minogue", "")
        song8 = Song("Success", "Danni Minogue", "")
        song9 = Song("So Hard To Forget", "Danni Minogue", "")
        song10 = Song("Beliver", "", "Rogue Traders")
        song11 = Song("Voodoo Child", "", "Rogue Traders")
        song12 = Song("Way To Go!", "", "Rogue Traders")
        song13 = Song("Stay", "", "Shakespears Sister")
        song14 = Song("I Don't Care", "", "Shakespears Sister")
        song15 = Song("Moonchild", "", "Shakespears Sister")
        song16 = Song("Heart Of Glass", "", "Blondie")
        song17 = Song("Denis", "", "Blondie")
        song18 = Song("Atomic", "", "Blondie")
        playlist1 = [song1, song2, song3, song4, song5, song6, song7, song8, song9]
        playlist2 = [song10, song11, song12, song13, song14, song15, song16, song17, song18]
        guest1 = Guest("James", 100, "Rockferry")
        guest2 = Guest("Meg", 50, "Don't Stop Me Now")
        guest3 = Guest("David", 5, "Can't Get You Out Of My Head")
        guest4 = Guest("Tracy", 20, "Atomic")
        guest5 = Guest("Carol", 30, "Heart Of Glass")
        guest6 = Guest("Steven", 40, "Voodoo Child")
        guest7 = Guest("Norma", 55, "Love And Kisses")
        guest9 = Guest("Michael", 60, "Stay")
        guest10 = Guest("Hugh", 70, "Denis")
        guest11 = Guest("Alan", 80, "Success")
        guests1 = [guest1, guest2]
        guests2 = [guest6, guest7]
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

    def test_room_find_guest_by_name(self):
        self.assertIsNotNone(self.room1.guests[0], self.room1.find_guest_by_name("Meg"))