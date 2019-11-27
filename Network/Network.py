from .Neuron import Neuron


class Network():
    def __init__(self, coutNeurons: list):
        self.matrix = []
        for i in coutNeurons:
            self.matrix.append([Neuron() for _ in range(i)])

    def __str__(self):
        result = ""
        for layer in self.matrix:
            for neuron in layer:
                result += str(neuron) + " "
            result += "\n"
        return result
