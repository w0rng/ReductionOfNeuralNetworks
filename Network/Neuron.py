from random import uniform as rand


class Neuron:
    def __init__(self, weight: list = None, ) -> None:
        self._weight = weight if weight else []

    def gen_weight(self, cout: int) -> None:
        self.weight = [rand(-0.5, 0.5) for _ in range(cout)]
