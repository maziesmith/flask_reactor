class Pychronium:
    """
    Pychronium is an energy source recovered from a recent supernova event in the andromeda galaxy. <br>
    Pychronium absorbs reactant nucleii and transmutates all subatomic particles into pychron.
    """

    def __init__(self):
        self.name = 'pychronium'
        self.energy_level = 67108864

    def __repr__(self):
        return f"*{self.name}*"

    def pychron(self):
        print('This is a block of Pychronium.')
        




def main():
    pychron = Pychronium()
    print(pychron)
    print(pychron.energy_level)


if __name__ == "__main__":
    main()