__author__ = 'fhca'

"""
           P|S
         1_1|1_1
        2_22|22_2
       3_33.|.33_3
      4_4...|.444_4
     5_555..|.5555_5
"""

import numpy as np


def dibujo(pr, tamaño, jugadores, turno):
    """pr es una lista de dos elementos que son a su vez listas.
    tamaño = 'chico' (5 renglones) o 'grande' (10 renglones).
    jugadores = arreglo de dos nombres.
    turno = 0 o 1."""
    if tamaño == 'chico':
        tam = 5
        dim = 15
    else:
        tam = 10
        dim = 25
    d = np.array([[' '] * dim] * dim, dtype=str)
    mitad = dim // 2
    d[:, mitad] = '|'  # //= división entera
    r = 1
    d[r, mitad - 1] = jugadores[0][0]  # 1er caracter del 1er nombre
    d[r, mitad + 1] = jugadores[1][0]  # 1er caracter del 2o nombre
    r += 1
    for n in range(1, tam + 1):
        d[r, mitad - n - 2] = str(n)
        d[r, mitad - n - 1] = '_'
        d[r, mitad + n + 2] = str(n)
        d[r, mitad + n + 1] = '_'
        d[r, mitad + 1:mitad + n + 1] = '.'
        d[r, mitad - 1:mitad - n - 1:-1] = '.'
        d[r, mitad - n:mitad - n + pr[0][n - 1]] = str(n)
        d[r, mitad + n:mitad + n - pr[1][n - 1]:-1] = str(n)
        r += 1
    if turno == 0:
        d[0, 2:7] = np.array(list('TURNO'))
    else:
        d[0, dim - 7:dim - 2] = np.array(list('TURNO'))
    return d


def imprime(d):
    """Imprime un dibujo desde una matriz d."""
    r, c = d.shape
    for ren in range(r):
        for col in range(c):
            print(d[ren, col], end=' ')
        print()


imprime(dibujo(pr=[[1, 2, 2, 1, 2], [1, 2, 2, 3, 4]], tamaño='chico',
               jugadores=['Paty', 'Samuel'], turno=1))
