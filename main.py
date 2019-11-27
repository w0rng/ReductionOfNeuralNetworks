from Network.Network import Network
from math import exp as e
from Network.Saver import Saver


def main():
    network = Network([1, 2, 3, 4, 3, 2, 1], lambda x: 1/(1+e(-x)))
    saver = Saver(network)


if __name__ == "__main__":
    main()
