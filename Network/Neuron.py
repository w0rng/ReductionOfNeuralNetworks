from random import uniform


class Neuron:
    def __init__(self, weight: float = None, inp: list = [], out: list = []):
        self.weight = weight if weight else uniform(-0.5, 0.5) 
        self.inp = inp
        self.out = out

    def __str__(self):
        return str(self.weight)
