class Room:
    def __init__(self, init_name, init_capacity, init_entryfee, init_playlist, init_guests):
        self.name = init_name
        self.capacity = init_capacity
        self.entryfee = init_entryfee
        self.playlist = init_playlist
        self.guests = init_guests

# find the room by name
    # def find_room_by_name(self, room_name):
    #     return [room for room in self.rooms if guest.name == guest_name]
        
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
        if self.reduce_guest_wallet(new_guest, self.entryfee) and len(self.guests) < self.capacity:
            self.guests.append(new_guest)
            if self.find_song_by_title(new_guest.favsong) != None:
                print("Whoo! They have my favourtie song!")
        else:
            print("Room is full")

# check out a guest
    def check_out_guest(self, guest_name):
        self.guests.remove(self.find_guest_by_name(guest_name))

# add a song to the playlist

# remove a song from the playlist

# return number of guests in room

# check the capacity of the room

# favourite song on the playlist
