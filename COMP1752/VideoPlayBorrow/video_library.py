from library_item import LibraryItem

class LibraryItem:
    def __init__(self, name, director, rating=0, play_count = 0):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars

library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
library["02"] = LibraryItem("Naruto", "Masashi Kishimoto", 5)
library["03"] = LibraryItem("Conan", "Aoyama Gōshō", 1)
library["04"] = LibraryItem("One Piece", "Eiichiro Oda", 3)
library["05"] = LibraryItem("Doraemon", "Fujiko Fujio", 4)


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
        return item.play_count  # Return the updated play count
    except KeyError:
        return None  # Return None if the key is not found

