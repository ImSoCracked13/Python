class MusicPlayer:
    def init(self):
        self.name = "Music Player"
        self.type = "Volume"
        self.level = 10
        self.status = True
    # turn on
    def turn_on(self):
        self.status = True
        print("Music player is on")
    # turn off
    def turn_off(self):
        self.status = False
        print("Music player is off")
    # increase the temp
    def increase(self):
        self.status += 1
        print(f"Music player volume has increased by {self.level}")
    # decrease the temp
    def decrease(self):
        self.status -= 1
        print(f"Heating temperature has decreased by {self.level}")
    
    def play(self):
        print(f"Music player is playing {self.song[self.current_song]}")
    
    def pause(self):
        print(f"Music player is paused")

    def next(self):
        self.current_song = (self.current_song + 1) % len(self.song)
        # if self.current_song == len(self.songs):
            # self.current_song = 0
        print(f"Music player is forwarded to play {self.current_song}")

    def previous(self):
        self.current_song = (self.current_song - 1) % len(self.song)
        print(f"Music player is backwarded to play {self.current_song}")
