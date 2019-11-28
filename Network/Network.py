from .Neuron import Neuron
import json
from types import FunctionType
from .Saver import State


class Network():
    def __init__(self, cout_neurons: list, activation: FunctionType, dx: FunctionType) -> None:
        self.activation = activation
        self.dx = dx
        if len(cout_neurons) >= 2:
            self._create_matrix(cout_neurons)
        else:
            exit(2)

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

    def predict(self, data: list) -> list:
        data = self._data_normalization(data)
        for i, layer in enumerate(self.matrix):
            for j, neuron in enumerate(layer):
                if i == 0:
                    neuron.inp = data[j]
                else:
                    inp = [n.inp * n.weight[j] for n in self.matrix[i - 1]]
                    neuron.inp = self.activation(sum(inp))
        return [self.activation(n.inp) for n in self.matrix[-1]]

    def _data_normalization(self, data: list) -> list:
        return [elem/max(data) for elem in data]

    def _save(self) -> State:
        return State(self.matrix)

    def _restore(self, state: State) -> None:
        self.matrix = state.get_weights()

    """     def trainig(self, data: list, expected: list, learning_rate: int) -> None:
        self.predict(data)
        errors = [predict[i] - expected[i] for i in range(len(predict))]
        weight_delta = [error * self.dx(predict[i])
                        for i, error in enumerate(errors)]
        print(weight_delta)
        for i, layer in self.matrix[-1]:
            for j, neuron in layer:
                pass """
