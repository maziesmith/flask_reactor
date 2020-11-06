from database.elements import periodic_table
from utilities.conversions import fahrenheit_to_celsius


def top_melting_point():
    highest_melting_point = {
        'element': None,
        "temp": 0
    }

    for item in periodic_table:
        if item['melting point'] > highest_melting_point['temp']:
            highest_melting_point['temp'] = item['melting point']
            highest_melting_point['element'] = item['element']

    return (highest_melting_point['element'], highest_melting_point['temp'])


def bottom_melting_point():
    lowest_melting_point = {
        'element': None,
        'temp': 0
    }

    for item in periodic_table:
        if item['melting point'] < lowest_melting_point['temp']:
            lowest_melting_point['temp'] = item['melting point']
            lowest_melting_point['element'] = item['element']

    return (lowest_melting_point['element'], lowest_melting_point['temp'])


def top_boiling_point():
    highest_boiling_point = {
        'element': None,
        "temp": 0
    }

    for item in periodic_table:
        if item['boiling point'] > highest_boiling_point['temp']:
            highest_boiling_point['temp'] = item['boiling point']
            highest_boiling_point['element'] = item['element']

    return (highest_boiling_point['element'], highest_boiling_point['temp'])


def bottom_boiling_point():
    lowest_boiling_point = {
        'element': None,
        "temp": 0
    }

    for item in periodic_table:
        if item['boiling point'] < lowest_boiling_point['temp']:
            lowest_boiling_point['temp'] = item['boiling point']
            lowest_boiling_point['element'] = item['element']

    return (lowest_boiling_point['element'], lowest_boiling_point['temp'])


def greatest_mass():
    mass = {
        'element': None,
        "atomic weight": 0
    }

    for item in periodic_table:
        if item['atomic weight'] > mass['atomic weight']:
            mass['atomic weight'] = item['atomic weight']
            mass['element'] = item['element']

    return (mass['element'], mass['atomic weight'])