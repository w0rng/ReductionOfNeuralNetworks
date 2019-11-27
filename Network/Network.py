from .Neuron import Neuron
import json
from types import FunctionType
from .Saver import State


class Network():
    def __init__(self, cout_neurons: list, activation: FunctionType) -> None:
        self._activation = activation

        if len(cout_neurons) >= 2:
            self._create_matrix(cout_neurons)

    def _create_matrix(self, cout_neurons: list) -> None:
        self.matrix = []
        for cout in cout_neurons:
            self.matrix.append([Neuron() for _ in range(cout)])
        self._gen_weights(cout_neurons)

    def _gen_weights(self, cout_neurons: list) -> None:
        for i, layer in enumerate(self.matrix):
            for neuron in layer:
                if i != len(self.matrix)-1:
                    neuron.gen_weight(cout_neurons[i + 1])
                else:
                    neuron.weight = [1]

    def _save(self) -> State:
        return State(self.matrix)

    def _restore(self, state: State) -> None:
        self.matrix = state.get_weights()
