import unittest
from classes.Song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Rockferry", "Duffy", "")
        self.song2 = Song("Voodoo Child", "", "Rogue Traders")

    def test_song_has_title(self):
        self.assertEqual("Rockferry", self.song1.title)
        self.assertEqual("Voodoo Child", self.song2.title)

    def test_song_has_artist(self):
        self.assertEqual("Duffy", self.song1.artist)
        self.assertEqual("", self.song2.artist)

    def test_song_has_band(self):
        self.assertEqual("", self.song1.band)
        self.assertEqual("Rogue Traders", self.song2.band)
