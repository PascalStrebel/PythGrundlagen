# This is a sample Python script.
import numpy as np
import scipy as sp
import scipy.misc
import scipy.integrate
from matplotlib import pyplot as plt


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

def f(x):
    return x ** 3 - 10 * np.sin(x) - 4

def df(x):
    return sp.misc.derivative(f, x)

@np.vectorize
def F(x):
    return sp.integrate.quad(f, 0, x)[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    X = np.linspace(-3, 3, 100)

    Y = f(X)
    Y1 = df(X)
    Y2 = F(X)

    plt.plot(X, Y, linewidth=2, label="$f$")
    plt.plot(X, Y1, linewidth=2, linestyle="dashed", label="$f'$")
    plt.plot(X, Y2, linewidth=2, linestyle="dotted", label="$F$")
    plt.legend()
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
