from random import uniform as rand


class Neuron:
    def __init__(self, weight: list = [], inp: list = []):
        self.weight = weight
        self.inp = inp

    def genWeight(self, cout: int):
        self.weight = [rand(-0.5, 0.5) for _ in range(cout)]
