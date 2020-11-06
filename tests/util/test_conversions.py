from utilities.conversions import fahrenheit_to_celsius, celsius_to_fahrenheit


def test_c_to_f():
    assert celsius_to_fahrenheit(25) == 77


def test_f_to_c():
    assert fahrenheit_to_celsius(77) == 25