__author__ = 'fhca'


def ceros_forma1(m, n):
    """Matriz (arreglo bidimensional) que contiene ceros de m por n."""
    matriz = list()
    for r in range(m):
        renglon = list()
        for i in range(n):
            renglon.append(0)
        matriz.append(renglon)
    return matriz


import numpy as np


def ceros_forma2(m, n):
    """Construye matriz de ceros (arreglo bidimensional) que
    contiene ceros, de mxn usando Numpy"""
    return np.zeros((m, n))  # agregar "dtype=int" si quieres una mat de enteros


def ceros_forma3(m, n):
    """Matriz (arreglo bidimensional) que contiene ceros de m por n."""
    matriz = tuple()
    for r in range(m):
        renglon = tuple()
        for i in range(n):
            renglon.append(0)  # ERROR!, no puedo agregar elem a una tupla
        matriz.append(renglon)
    return matriz


c = ceros_forma2(5, 4)
print("c[1]=", c[1])
print("c=", c)
# esta notación funciona con lista de listas y con numpy
c[2][3] = 5
c[3][3] = 6
print("c=", c)

# esto solo funciona con numpy
c[1, 1] = 4
c[2, 2] = 3
print("4 y 3 agregados:")
print(c)
print("------------------")

print("REBANADAS (slides)")
c = ceros_forma2(60, 40)

c[:, 0] = 1
c[1, :] = 2
c[57:59, 37:39] = 10

d = np.array([[1, 2], [3, 4]])
c[0:2, 37:39] = d
print(c)
print("Acceso LUJOSO (fancy)")
c = ceros_forma2(60, 40)
c[57, 1] = 8
c[58, 2] = 8
c[59, 2] = 8

c[[57, 58, 59], [38, 39, 39]] = np.array([1, 2, 3])

c[[0, 2], 1] = 5
c[1, [37, 38]] = 7

print(c)

print("Pasando de lista de listas a array de numpy")
c = ceros_forma1(60, 40)
print(c)
c = np.array(c)  # ahora c es un arreglo de numpy y lo podemos trabajar como arriba.
print(c)
