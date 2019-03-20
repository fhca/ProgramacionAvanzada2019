__author__ = 'fhca'

# cargar la biblioteca numpy de cálculos numéricos
import numpy as np

"""Definición de cículo:
Es el lugar geométrico de los puntos cuya distancia a un punto fijo (llamado centro), es 
menor que un valor fijo (llamado radio).

d(x, y)= sqrt((x_1 - y_1)**2 + (x_2 - y_2)**2)
Distancia Euclidiana - Métrica usual en R**2
"""


def montecarlo():
    n = 1000000000
    puntos = np.random.rand(2 * n).reshape((n, 2))
    centro = np.array([.5, .5])
    dist_cuadrado = np.sum((puntos - centro) ** 2, axis=1)
    puntos_en_circulo = np.sum(dist_cuadrado < .25)
    return 4 * puntos_en_circulo / n


def montecarlo2():
    n = 1000000000
    centro = np.array([.5, .5])
    puntos_en_circulo = 0
    for i in range(n):
        punto = np.random.rand(2)
        dist_cuadrado = np.sum((punto - centro) ** 2)
        if dist_cuadrado < .25:
            puntos_en_circulo += 1  # incrementa el num de puntos dentro del círculo
    return 4 * puntos_en_circulo / n


print(montecarlo2())
