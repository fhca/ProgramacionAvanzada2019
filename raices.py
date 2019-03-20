__author__ = 'fhca'

import numpy as np
import matplotlib.pyplot as plt   # biblioteca para graficar


def raiz_cuadrada(n):
    "Calcula la raiz cuadrada de un valor por el método Babilónico."
    pasos = 10000
    x0 = 1
    xant = 1
    error = 1e-5
    for _ in np.arange(pasos):
        x0 = (x0 + n / x0) / 2
        if np.abs(x0 - xant) < error:
            break
        xant = x0
    print("numero de pasos:", _)
    return x0


print(raiz_cuadrada(65610000*65610000))

"""
graficando
plt.figure()
pasos = np.arange(1, 11, dtype=int)
y = [raiz_cuadrada(100000, p) for p in pasos]
plt.plot(pasos, y)
plt.show()
"""
