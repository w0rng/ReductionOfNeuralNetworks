from .Neuron import Neuron
import json
from types import FunctionType


class Network():
    def __init__(self, coutNeurons: list, activationFunc: FunctionType):

        self.activation = activationFunc

        if len(coutNeurons) >= 2:
            self.createMatrix(coutNeurons)
            self.linkBuild()

            # добавляем связи
            for i, layer in enumerate(self.matrix):
                for neuron in layer:
                    if i != len(self.matrix)-1:
                        neuron.out = self.matrix[i + 1]
                        neuron.genWeight(coutNeurons[i+1])

    def createMatrix(self, coutNeurons: list):
        self.matrix = []
        for i in coutNeurons:
            self.matrix.append([Neuron() for _ in range(i)])

    def linkBuild(self):
        for i, layer in enumerate(self.matrix):
            for neuron in layer:
                if i != len(self.matrix)-1:
                    neuron.out = self.matrix[i + 1]

    def save(self, fileName: str):
        with open(fileName, "w") as file:
            data = {}
            for i, layer in enumerate(self.matrix):
                data[i] = {}
                for j, neuron in enumerate(layer):
                    data[i][j] = neuron.weight
            json.dump(data, file)

    def load(self, fileName: str):
        coutNeurons = []
        with open(fileName, "r") as file:
            data = json.loads(file.read())
            """ self.createMatrix(coutNeurons)
            self.linkBuild() """
            for layer in data:
                coutNeurons.append(len(data[layer]))
                print(coutNeurons)
                newLayer = [data[layer][neuron] for neuron in data[layer]]
                self.matrix.append(newLayer)
