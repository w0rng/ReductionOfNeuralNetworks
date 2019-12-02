from math import exp as e

from Network.Network import Network
from Network.Saver import Saver


def main():
    network = Network([3, 2, 1], activation, dx)
    saver = Saver(network)
    print(network.predict([1, 1, 0]))
    network.trainig([1, 1, 0], [0], 0.1)


def activation(x):
    return 1 / (1 + e(-x))


def dx(x):
    return activation(x)*(1-activation(x))


if __name__ == "__main__":
    main()
