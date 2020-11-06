from database.random import find_random_element


def test_random_element():
    random_element = find_random_element()
    assert random_element != None