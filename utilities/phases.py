from database.elements import periodic_table

def phase_finder(ele, temp):
    element = ele.lower()
    for x in periodic_table:
        if (x['element'] == element):
            if (temp <= x['melting point']):
                return 'solid'
            elif (temp > x['melting point'] and temp < x['boiling point']):
                return 'liquid'
            elif (temp >= x['boiling point']):
                return 'gas'
    
    raise Exception("This input is invalid. Please check your spelling")