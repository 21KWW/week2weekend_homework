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
        # print(self.guests)
        return [guest for guest in self.guests if guest.name == guest_name]

# check in a guest

# check out a guest

# add a song to the playlist

# remove a song from the playlist

# return number of guests in room

# check the capacity of the room

# favourite song on the playlist
