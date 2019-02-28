__author__ = 'fhca'

import time
import numpy as np


def muestra(f, *param):
    t0 = time.time()
    r = f(*param)
    t1 = time.time()
    print("tiempo:", t1 - t0, "resultado:", r)
    return r


def factorial1(n):
    """ 1 x 2 x 3 x 4 x 5 x ... x n. """
    mult = 1  # elemento neutro de la multiplicación, INCIALIZA LA MULTIPLICACIÓN
    for i in range(2, n + 1):
        mult *= i  # mult = mult * i
    return mult


def factorial2(n):
    return np.prod(np.arange(1, n + 1, dtype=float), dtype=np.uint64)


"""
# ejemplos del factorial
v = 400
vf1 = muestra(factorial1, v)
print("vf1 % 2**64:", vf1 % 2**64)
muestra(factorial2, v)
"""


def combinaciones(s, n):
    from scipy.special import comb
    return comb(s, n, exact=True)


import matplotlib.pyplot as plt

plt.figure()
def grafica(s):
    x = np.arange(0, s + 1)
    y = []
    for n in x:
        y.append(combinaciones(s, n))

    plt.plot(x, y)

for s in range(100):
    grafica(s)

plt.show()
