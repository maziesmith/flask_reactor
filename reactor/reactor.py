from random import randint
from .pychronium import Pychronium
from .reactant import Reactant

#           reactant
#      ^     /   \     >
#           /     \
#   reactant       reactor
#           \     / 
#      <     \   /     v
#            result



#  element + element => FlaskReactor  => new element


class FlaskReactor:
    """
    A particle accelerator that produces a nuclear transmutation product. 
    The elements will undergo transmutation with pychronium and produce a newly formed element. 
    """
    prefixes = ['Man', 'Cys', 'Dil', 'Gon', 'Am', 'Cent', 'Demos', 'Graph', 'Terr', 'Vita', 'Mar', 
    'Port', 'Aud', 'Antro', 'Sub', 'Ab', 'An', 'Co', 'Mal', 'Trans', 'Un']
    suffixes = ['gen', 'ium', 'ine', 'ide', 'on', 'ous', 'ary', 'ant', 'ion']
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    opacities = ['0.8']

    def __init__(self, accelerant=None, prima_materia_unico=None, prima_materia_secondo=None):
        self.accelerant = accelerant
        self.prima_materia_unico = prima_materia_unico
        self.prima_materia_secondo = prima_materia_secondo
        self.vessel_id = randint(1, 5000)
        self.temperature = 0
        self.magnetized = False
        self.pychronium_status = ''
        self.energy = None
        self.magnum_opus = {
            'name': None,
            'melting point': None,
            'boiling point': None,
            'symbol' : None,
            'atomic pychrons': None,
            'phase': None,
            'weight': None,
            'color': None,
            'opacity': None,
            'description': None
        }

    def __repr__(self):
        return f"Reactor# {self.vessel_id}"


    def heating(self):
        self.temperature = 2**28
        return self.temperature


    def magnetic_confinement(self):
        if (self.temperature > 100000000):
            self.magnetized = True
            return f'magnetized at {self.temperature}'

    def pychronium_beam_injection(self, plasma_soup):
        if (plasma_soup == f'magnetized at 268435456' and self.magnetized == True):
            reactant_one = self.prima_materia_unico
            reactant_two = self.prima_materia_secondo
            melting_difference = None
            melting_mutation = None
            boiling_difference = None
            boiling_mutation = None
            boiling_point = None
            phase = None
            subatomic_count = (int(reactant_one['atomic number']) + int(reactant_two['atomic number']) * 2)
            self.energy = self.temperature / self.accelerant.energy_level
            self.magnum_opus['atomic pychrons'] = subatomic_count + round(((self.energy - 1)/10) * subatomic_count)
            if reactant_one['melting point'] > reactant_two['melting point']:
                melting_difference = reactant_one['melting point'] - reactant_two['melting point']
                melting_mutation = int(melting_difference) + int(round(self.energy))
                self.magnum_opus['melting point'] = abs(round(int(reactant_one['melting point']) * (0.05 * melting_mutation))) - 800
            else:
                melting_difference =  reactant_two['melting point'] - reactant_one['melting point']
                melting_mutation = int(melting_difference) + int(round(self.energy))
                self.magnum_opus['melting point'] = abs(round(int(reactant_two['melting point']) * (0.05 * melting_mutation))) - 800
            if reactant_one['boiling point'] > reactant_two['boiling point']:
                boiling_difference = reactant_one['boiling point'] - reactant_two['boiling point']
                boiling_mutation = int(boiling_difference) + int(round(self.energy))
                self.magnum_opus['boiling point'] = abs(round(int(reactant_one['boiling point']) * (0.05 * boiling_mutation))) - 700
            else:
                boiling_difference =  reactant_two['boiling point'] - reactant_one['boiling point']
                boiling_mutation = int(boiling_difference) + int(round(self.energy))
                self.magnum_opus['boiling point'] = abs(round(int(reactant_two['boiling point']) * (0.05 * boiling_mutation))) - 700
            if int(self.magnum_opus['melting point']) > 77:
                self.magnum_opus['phase'] = 'solid'
            elif (int(self.magnum_opus['melting point']) < 77 and int(self.magnum_opus['boiling point']) > 77):
                self.magnum_opus['phase'] = 'liquid'
            else:
                self.magnum_opus['phase'] = 'gas'
            x = randint(0, 20)
            y = randint(0, 8)
            pre = FlaskReactor.prefixes[x]
            suf = FlaskReactor.suffixes[y]
            self.magnum_opus['name'] = f'Py{pre}{suf}'
            self.magnum_opus['symbol'] = 'Py'+ pre[0:2]
            self.magnum_opus['weight'] = round(((float(reactant_one['atomic weight']) + float(reactant_two['atomic weight']))/2) * 3)
            col_int = randint(0, 6)
            self.magnum_opus['color'] = FlaskReactor.colors[col_int]
            self.magnum_opus['opacity'] = FlaskReactor.opacities[0]
            self.pychronium_status = 'Injected'
            return f'<*>pychronium beam injected<*>'

        


    def cooling(self):
        capitalized_name = self.magnum_opus['name'].capitalize()
        self.magnum_opus['description'] = f'{capitalized_name} is a {self.magnum_opus["color"]}ish {self.magnum_opus["phase"]} with {self.magnum_opus["atomic pychrons"]} pychrons!'
        return self.magnum_opus




def main():
    TEST_HYDROGEN = {
        "atomic number": 1,
        "element": "hydrogen",
        "atomic weight": 1.008,
        "class": "nonmetal",
        "phase": "gas",
        "period": 1,
        "electron config": '1s1',
        "melting point": -434.5,
        "boiling point": -423.2,
        "symbol": "H",
    }

    TEST_HELIUM = {
        "atomic number": 2,
        "element": "helium",
        "atomic weight": 4.003,
        "class": "noble gas",
        "phase": "gas",
        "period": 1,
        "electron config": '1s2',
        "melting point": -458,
        "boiling point": -452.1,
        "symbol": "He"
    }

    reaction = FlaskReactor(Pychronium(),TEST_HYDROGEN, TEST_HELIUM)
    attrs = vars(reaction)
    print(reaction.heating())
    print(reaction.magnetic_confinement())
    print(reaction.pychronium_beam_injection('magnetized at 268435456'))
    print(reaction.cooling())
    # print(', '.join("%s: %s" % item for item in attrs.items()))



if __name__ == "__main__":
    main()