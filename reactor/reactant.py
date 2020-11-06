class Reactant:
    """
    A reactant for a chemical reaction.
    """
    def __init__(self, name, atomicnumber, weight, melting, boiling, symbol, phase):
        self.name = name
        self.atomicnumber = atomicnumber
        self.weight = weight
        self.melting = melting
        self.boiling = boiling
        self.symbol = symbol
        self.phase = phase


    def __repr__(self):
        return f"Reactant: {self.name}"


def main():
    reactant = Reactant('Hydrogen', 1, 1.008, -434.5, -423.2, 'H', 'gas')
    attrs = vars(reactant)
    print(', '.join("%s: %s" % item for item in attrs.items()))
    print(reactant)


if __name__ == "__main__":
    main()