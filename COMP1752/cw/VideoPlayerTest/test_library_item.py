
# A seperated file to take part as a Library Class and its function is the root.
class LibraryItem:
    def __init__(self, name, director, rating=0):
        self.name = name # Set name
        self.director = director # Set artist
        self.rating = rating # Set Rating stars
        self.play_count = 0 # Set play count


# A default text for informative display and this is for the video_library operation
    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"


# Function for numerical rating become actual stars by using asterisk symbol = "*" 
    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
