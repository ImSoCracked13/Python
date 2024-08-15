from library_item import LibraryItem

def test_name():
    test = LibraryItem("The Rumbling", "SiM", 5)
    assert test.name == "The Rumbling"

def test_director():
    test = LibraryItem("The Rumbling", "SiM", 5)
    assert test.director == "SiM"

def test_rating():
    test = LibraryItem("The Rumbling", "SiM", 5)
    assert test.rating == 5

def test_info():
    test = LibraryItem("Never Fear", "Mao Abe", 4)
    assert test.info() == "Never Fear - Mao Abe ****"

def test_stars():
    test = LibraryItem("Never Fear", "Mao Abe", 8)
    assert test.stars() == "********"

def test_play_count_initialization():
    test = LibraryItem("Blizzard", "Daichi Miura", 4)
    assert test.play_count == 0

def test_play_count_increment():
    test = LibraryItem("Blizzard", "Daichi Miura", 4)
    test.play_count += 10
    assert test.play_count == 10


