from utilities.aggregates import greatest_mass, top_boiling_point, top_melting_point, bottom_boiling_point, bottom_melting_point

def test_top_melting_point():
    x = top_melting_point()
    assert x[0] == 'carbon'
    assert x[1] == 6420


def test_bottom_melting_point():
    x = bottom_melting_point()
    assert x[0] == 'helium'
    assert x[1] == -458

def test_top_boiling_point():
    x = top_boiling_point()
    assert x[0] == 'niobium'
    assert x[1] == 8901

def test_bottom_boiling_point():
    x = bottom_boiling_point()
    assert x[0] == 'helium'
    assert x[1] == -452.1

def test_greatest_mass():
    x = greatest_mass()
    assert x[0] == 'tin'
    assert x[1] == 118.71