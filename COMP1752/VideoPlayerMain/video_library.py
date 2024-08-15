# An existed module of Python to work as forming a Window-like application
from library_item import LibraryItem


# A manual editing area for changing current existed data of the video list
library = {}
library["00"] = LibraryItem("Idol", "YOASOBI", 5)
library["01"] = LibraryItem("Crossing Field", "LiSa", 4)
library["02"] = LibraryItem("STYX HELIX", "Myth & Roid", 4)
library["03"] = LibraryItem("Unravel", "TK", 5)
library["04"] = LibraryItem("Lost in Paradise", "ALI ft.AKLO", 3)
library["05"] = LibraryItem("Hey Kids!!", "Kyouran", 2)
library["06"] = LibraryItem("Crying for Rain", "Minami", 3)
library["07"] = LibraryItem("only my railgun", "fripSide", 2)
library["08"] = LibraryItem("Mephisto", "Queen Bee", 1)
library["09"] = LibraryItem("Black Catcher", "Vickeblanka", 1)


# This function is for showing every information in the simple database function
def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


# A function used for getting name of the video when browsing or editting 
def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


# A function used for getting artists name of the video when browsing or editting
def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


# A function used for getting rating stars of the video when browsing or editting
def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


# A function for appearing number of play count
def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


# A function for noticing how many time of the video has runned
def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return


# A function to update/fix the rating to a new rating
def update_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


# A function to save video to the library
def save_video_library():
    data = []
    for key, item in library.items():
        data.append([key, item.name, item.director, item.rating, item.play_count])

