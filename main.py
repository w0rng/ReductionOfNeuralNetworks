from Network.Network import Network
from math import exp as e


def main():
    network = Network([1, 2, 3, 4, 3, 2, 1], activation)
    network.load("weight.json")
    network.save("weight.json")


def activation(x):
    return 1/(1+e(-x))


if __name__ == "__main__":
    main()
