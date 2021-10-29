from classes.Song import Song


class Room:
    def __init__(self, init_name, init_capacity, init_entryfee, init_playlist, init_guests):
        self.name = init_name
        self.capacity = init_capacity
        self.entryfee = init_entryfee
        self.playlist = init_playlist
        self.guests = init_guests
        
# find guest by name
    def find_guest_by_name(self, guest_name):
        for guest in self.guests:
            if guest.name == guest_name:
                return guest
        return None
        # [ result = guest for guest in self.guests if guest.name == guest_name ]
        # return result

# find a song by its title
    def find_song_by_title(self, song_title):
        for song in self.playlist:
            if song.title == song_title:
                return song
        return None

# reduce the money in the guest wallet
    def reduce_guest_wallet(self, guest, cash):
        if guest.wallet >= cash:
            guest.wallet -= cash
            return True
        else:
            return False

# check in a guest
    def check_in_guest(self, new_guest):
        if self.reduce_guest_wallet(new_guest, self.entryfee) and self.check_room_capacity():
            self.guests.append(new_guest)
            self.check_favsong(new_guest.favsong)
        else:
            print("Room is full")

# check out a guest
    def check_out_guest(self, guest_name):
        self.guests.remove(self.find_guest_by_name(guest_name))

# add a song to the playlist
    def add_song_to_playlist(self, new_song):
        self.playlist.append(new_song)

# remove a song from the playlist
    def remove_song_from_playlist(self, song_title):
        self.playlist.remove(self.find_song_by_title(song_title))

# return number of guests in room
    def check_num_guests(self):
        return len(self.guests)

# check the capacity of the room
    def check_room_capacity(self):
        if len(self.guests) < self.capacity:
            return True
        else:
            return False

# favourite song on the playlist
    def check_favsong(self, song_name):
        if self.find_song_by_title(song_name) != None:
            print("Whoo! They have my favourtie song!")
            return True
