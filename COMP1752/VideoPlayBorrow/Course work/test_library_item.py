from library_item import LibraryItem

def test_name1():
    test = LibraryItem("Duy Anh", "Beo", 5)
    assert test.name == "Duy Anh"

def test_name2():
    test = LibraryItem("Duy Anh", "Beo", 5)
    assert test.name == "Duy Anhh"

def test_director1():
    test = LibraryItem("Duy Anh", "Beo", 5)
    assert test.director == "Beo"

def test_director2():
    test = LibraryItem("Duy Anh", "Beo", 5)
    assert test.director == "Beo0"

def test_rating1():
    test = LibraryItem("Duy Anh", "Beo", 5)
    assert test.rating == 5

def test_rating2():
    test = LibraryItem("Duy Anh", "Beo", 5)
    assert test.rating == 6

def test_info1():
    test = LibraryItem("Duy Anh", "Beo", 4)
    assert test.info() == "Duy Anh - Beo ****"

def test_info2():
    test = LibraryItem("Duy Anh", "Beo", 4)
    assert test.info() == "Duy Anhh - Beo0 *****"

def test_stars1():
    test = LibraryItem("Duy Anh", "Beo", 4)
    assert test.stars() == "****"

def test_stars2():
    test = LibraryItem("Duy Anh", "Beo", 4)
    assert test.stars() == "*****"

def test_play_count_initialization1():
    test = LibraryItem("Duy Anh", "Beo", 4)
    assert test.play_count == 0

def test_play_count_initialization2():
    test = LibraryItem("Duy Anh", "Beo", 4)
    assert test.play_count == 1

def test_play_count_increment1():
    test = LibraryItem("Duy Anh", "Beo", 4)
    test.play_count += 10
    assert test.play_count == 10

def test_play_count_increment2():
    test = LibraryItem("Duy Anh", "Beo", 4)
    test.play_count += 10
    assert test.play_count == 11


