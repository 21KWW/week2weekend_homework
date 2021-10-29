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
        guest7 = Guest("Norma", 55, "Moonchild")
        guest9 = Guest("Michael", 60, "Stay")
        guest10 = Guest("Hugh", 70, "Denis")
        guest11 = Guest("Alan", 80, "Atomic")
        guests1 = [guest1, guest2]
        guests2 = [guest6, guest7]
        self.room1 = Room("Chill Room", 5, 5, playlist1, guests1)
        self.room2 = Room("Blue Room", 10, 10, playlist2, guests2)

    def test_room_has_name(self):
        self.assertEqual("Chill Room", self.room1.name)
        self.assertEqual("Blue Room", self.room2.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)
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
        self.assertEqual(self.room1.guests[1], self.room1.find_guest_by_name("Meg"))
        self.assertEqual(self.room2.guests[0], self.room2.find_guest_by_name("Steven"))

    def test_room_find_song_by_title(self):
        self.assertEqual(self.room1.playlist[0], self.room1.find_song_by_title("Rockferry"))
        self.assertEqual(self.room2.playlist[0], self.room2.find_song_by_title("Beliver"))

    def test_charge_guest_entryfee(self):
        self.room1.reduce_guest_wallet(self.room1.guests[0], self.room1.entryfee)
        self.assertEqual(95, self.room1.guests[0].wallet)
        self.room2.reduce_guest_wallet(self.room2.guests[0], self.room2.entryfee)
        self.assertEqual(30, self.room2.guests[0].wallet)

    def test_check_in_guest(self):
        self.room1.check_in_guest(Guest("David", 5, "Can't Get You Out Of My Head"))
        self.assertEqual(3, len(self.room1.guests))
        self.room2.check_in_guest(Guest("Michael", 60, "Stay"))
        self.assertEqual(3, len(self.room2.guests))

    def test_check_out_guest(self):
        self.room1.check_out_guest(self.room1.guests[0].name)
        self.assertEqual(1, len(self.room1.guests))
        self.room2.check_out_guest(self.room2.guests[0].name)
        self.assertEqual(1, len(self.room2.guests))

    def test_check_in_too_many_guests(self):
        self.room1.check_in_guest(Guest("Carol", 30, "Heart Of Glass"))
        self.room1.check_in_guest(Guest("Michael", 60, "Stay"))
        self.room1.check_in_guest(Guest("Hugh", 70, "Denis"))
        self.room1.check_in_guest(Guest("Alan", 80, "Atomic"))
        self.assertEqual(5, len(self.room1.guests))

    def test_add_song_to_playlist(self):
        self.room1.add_song_to_playlist(Song("Atomic", "", "Blondie"))
        self.assertEqual(10, len(self.room1.playlist))
    
    def test_remove_song_from_playtlist(self):
        self.room1.remove_song_from_playlist("Love And Kisses")
        self.assertEqual(8, len(self.room1.playlist))

    def test_number_guests_in_room(self):
        self.assertEqual(2, self.room1.check_num_guests())

    def test_check_room_capacity(self):
        self.assertTrue(self.room1.check_room_capacity())
    
    def test_check_favsong(self):
        self.assertTrue(self.room1.check_favsong("Rockferry"))
        self.assertFalse(self.room1.check_favsong("Atomic"))