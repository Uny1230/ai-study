import numpy as np
from matplotlib import pyplot as plt

from sigmoid import sigmoid


def main():
    draw_sigmoid()


def draw_sigmoid():
    x = np.arange(-5, 5, 0.1)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()


if __name__ == '__main__':
    main()
