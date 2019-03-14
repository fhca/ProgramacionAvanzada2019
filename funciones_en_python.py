__author__ = 'fhca'

import numpy as np

"Definamos una función simple."


def f(x):  # <-- esta línea se llama 'encabezado' de la función
    """Documentación de la función 'f':
    :param x,  valor real
    :returns y, valor real, eleva x al cuadrado y le suma 7
    """
    return x ** 2 + 7  # esta es la regla para aplicarle a x
    x = 25  # esto ya no lo va a hacer, pues la función acaba con el return


"Una función puede no devolver valores."


def g():
    """Esta es la documentación de la función. Aquí se describe la función
    que es lo que hace, que parámetros lleva, es decir, como se llaman,
    que tipo de valores se espera para cada parámetro, y por último, que
    tipo de valor debe devolver la función."""
    print("A")
    # si no le ponemos "return valor", la función devuelve None


"uso:"
f(4)  # el 23 se pierde!!!
f(4) + 7  # el 30 se pierde!!!
print(f(4))  # internamente, x vale 4, devuelve 23, lo imprime.

g()  # me imprime "A"
print(g())  # imprime "A" y además imprime None

"""Cuando queremos un número 'indeterminado' de parámetros, usamos el asterisco:"""


def suma_2(a, b):
    """Suma dos valores."""
    return a + b


def suma_3(a, b, c):
    """Suma tres valores."""
    return a + b + c


def suma_n(*params):
    """acepta un número 'indeterminado' de parámetros.
    la variable 'params' es una lista internamente."""
    return sum(params)  # suma todos los elementos de la lista 'params'


"uso:"

print(suma_2(2, 3))  # devuelve 5
print(suma_3(4, 5, 6))  # devuelve 15
print(suma_n(5, 2, 4, 3, 3, 1, 2, 7))  # suma todos!, da 27

"""
Valores en Python:

Tipos de datos que pueden haber en Python.

type(objeto)  -> devuelve el nombre del tipo de objeto

"declaración de variables" decir de que tipo será el objeto que contendrá una variable.

Ej. en C:    int x; ... x = 7;   "int x" declara que "x" contendrá enteros...
NOTA: En Python NO HAY DECLARACIÓN DE VARIABLES!!!
NOTA2: EN Python NO HAY ESTRICTAMENTE VARIABLES
NOTA3: En Python le llamamos variables a "nombres" o "etiquetas" que le "colgamos" a un objeto 
para referirnos a él. Por ejemplo. x = 7 ...  x = "Hola Paty"... o sea, que no hay forma de saber en principio
que tipo de objeto contiene x, dado que no se declara.

Lenguaje "tipado" (con tipos de datos).- Los objetos pueden ser de varios tipos.  Python SI ES TIPADO.
Analizando que pasa cuando hacemos x=7 y dos lineas mas abajo hacemo x="Hola Paty", como "x" no "contiene"
al objeto que se le asigna, lo que existe EN MEMORIA (del programa que está corriendo en ese momento) 
en realidad es únicamente el objeto, NO "x". 
    

TIPO        Ejemplo     Descripción
object      ...         Casi todo en Python es un object (objeto)

int         7           valor numérico, que se puede operar   [inmutable]

float       7.0         valor numérico, "mas grande" que los enteros... [inmutable]

str         "hola Paty" String... sucesión de caracteres, las operaciones [inmutable]

tuple       (1,2,3)     tupla de objetos [inmutable] a[0]=5  (error, no puedo modificar el primer valor de la tupla)

list        [1,2,3]     lista de objetos [mutable]  a[0]=5  -> a se convierte en [5,2,3]

set         {1,2,3}     conjunto, no hay un orden para sus elementos y estos son únicos.

dict        {"platano":"banana", "manzana":"apple"}   Los diccionarios son parejas "llave":"valor"
Se pueden ver como conjuntos cuyo índice son las llaves.... {1:(4,2), 2:(9.5,4)} [mutable][iterable]
Las llaves no pueden ser mutables (de hecho, deben ser hasheables  (hasheable=al objeto le puedo aplicar
una función que me dé un valor único para un objeto dado. a=[1,2,3] no es hasheable por que primero que
nada es mutable, pero además, es el mismo objeto que a=[5,2,3]))





a = (1,2,3)
a.append(4)  -> ERROR!, las tuplas son inmutables.
b = [1,2,3]
b.append(4)  -> [1,2,3,4]

aa = list(a)
aa.append(4)
aa = tuple(aa)  -> (1,2,3,4)



"""


"Otra forma: utilizando una lista como parámatro."


def suma_n_otra(chivito):  # supongamos que siempre le pasaremos un lista
    """suma los elementos de la lista que se le pase.
    Es UN SÓLO PARÁMETRO, pero como es lista, puede
    tener muchos elementos.
    :param chivito: list   # <-- se sugiere que el parametro 'chivito' sea lista
    """
    return sum(chivito)


print(suma_n_otra([2, 3]))
"definamos una función con dos parámetros."


def g(x, y):
    """función 'asimétrica', osea, no da lo mismo g(x,y) que
    g(y, x). Por ejemplo g(1,7) da 23 y g(7,1) da 17."""
    return 2 * x + 3 * y


" supongamos que 'x' y 'y' están en una lista., como uso g?"

params = [1, 7]

"versión 1 (así se hace en la mayoría de los lenguajes (C, Java, etc.)"
x = params[0]
y = params[1]
print(g(x, y))

"versión 2 (pythonica, técnica de 'asignación de tupla de variables')"
x, y = params  # lo de la izq. del '=' es una tupla de variables
print(g(x, y))

"versión 3 (pythonica, 'desempaquetamiento') "
print(g(*params))

"""Parametros de default (parámetros opcionales).
Se usa para darle valores default a uno o más parámetros.
"""


def duplica1(x):
    "duplica el valor de x"
    return 2 * x


def duplica2(x, factor=2):
    "si el factor es 3, triplica!"
    return factor * x


"uso:"

print(duplica1(7))  # da 14
print(duplica2(7))  # da 14
print(duplica2(7, 3))  # da 21

"""IMPORTANTE: si ya pusiste al menos un parámetro de default,
todos los que sigan, también tienen que ser tener default."""


def duplica3(x, factor=2, sumando=0):
    """'sumando' TIENE que tener un valor default."""
    return factor * x + sumando


"Ej. Como defino un parámetro default en términos de otro?."


def area_rectangulo(base, altura="nada"):
    """Calcula el área de un rectángulo dadas base y altura, pero si no se dá la
    altura, queremos que la altura default sea igual a la base (un cuadrado).
    En este caso, el valor default para la altura no puede ser un valor válido
     (no puede ser ni entero ni real). Pongámosle una cadena, por ejemplo, y en el cuerpo de
     la función, la reasignamos."""
    if altura == "nada":
        altura = base
    return base * altura


"uso:"
print(area_rectangulo(7, 1))  # da 7
print(area_rectangulo(7))  # da 49

"CUIDADO al usar defaults booleanos, pues 0=False, otra cosa=True"


def area_triangulo(base, altura=False):
    if not altura:
        altura = base
    return (base * altura) / 2


print("triangulo:", area_rectangulo(4, 3))  # da 6
print(area_triangulo(4, 0))  # da 8, porque 0 es False, entonces hace (4 * 4) / 2

"""Parametros nombrados.
Hasta ahorita hemos usado parámetros POSICIONALES, o sea, la posición de los valores determina
a que parámetro se asignan dichos valores. Ej. area_triangulo(4, 0) el 4 es necesariamente la base
y el 0 es necesariamente la altura. 

Sin embargo al USAR una función, puedes ponerle el nombre de sus parámetros, además de su valor.
Por ejemplo area_triangulo(base=4, altura=10)

Con esto se gana que 
1. sea más claro el uso de los parámetros, pues se muestra el nombre en la llamada
2. puedes poner los parámetros en cualquier orden

PRECAUCIÓN: Si usas un parámetro con su nombre, todos los demás parámetros después de ese
también tienes que usarlos con su nombre.
"""


def hipotenusa(cateto1, cateto2):
    return np.sqrt(cateto1 ** 2 + cateto2 ** 2)


"uso:"
print(hipotenusa(3, 4))
print(hipotenusa(cateto1=3, cateto2=4))
print(hipotenusa(cateto2=4, cateto1=3))  # el orden no es relevante

"""Se pueden mezclar en el uso (o llamada) de una función, parámetros posicionales y nombrados.
La condición es que los posicionales SIEMPRE van al principio y los nombrados al final."""

"uso:"
print(hipotenusa(3, cateto2=4))  # cateto1=3, da 5
" hipotenusa(cateto2=4, 3)  # error: los posicionales siempre van al principio."
"x=cateto2  # error: cateto2 no existe afuera de la función"

x = 5
y = 6
print(hipotenusa(x, y))  # posicional
print(hipotenusa(cateto1=x, cateto2=y))  # nombrados

cateto1 = 3
cateto2 = 4
print(hipotenusa(cateto1, cateto2))  # da 5, uso posicional de parámetros
"""IMPORTANTE:
Aquí, la variable externa cateto1, NADA TIENE QUE VER con el parámetro llamado cateto1.
Es al momento en que se pasan como parámetro que se dá la relación. Por ejemplo:
"""
print(hipotenusa(cateto2, cateto1))  # da 5, uso posicional, internamente cateto1=4, y cateto2=3

"""Veamos como el parámetro cateto1 adquiere el valor de la variable cateto1 (3), lo mismo 
con cateto2 (4). Los nombres a la izq. del signo '=' son los parámetros, los de la derecha 
son los valores (asignadoa a variables externas)."""
print(hipotenusa(cateto2=cateto2, cateto1=cateto1))  # da 5, uso nombrado,

"""Aquí internamente cateto1=4, cateto2=3. A cateto2 NO se le asigna el valor del parámetro
cateto1, sino el valor de la variable externa llamada cateto1."""
print(hipotenusa(cateto1=cateto2, cateto2=cateto1))  # da 5, uso nombrado,

"""Hasta ahorita hemos usado parámetros nombrados de manera opcional. Al definir la función
se puede obligar su uso mediante un asterisco solitario."""

"Aquí los parámetros después del '*' deben ser nombrados."


def perimetro_pentágono(base, pared1, pared2, *, techo1, techo2):
    return base + pared1 + pared2 + techo1 + techo2


"uso:"
print(perimetro_pentágono(1, 2, 3, techo1=4, techo2=5))  # da 15
"el orden puede variar si uso mas parámetros nombrados."
print(perimetro_pentágono(1, 2, techo1=4, techo2=5, pared2=3))  # da 15

"""Extras: Valores de verdad..."""
if "Falso":
    print("La cadena 'Falso' es True")

if "":
    print("cierto")
else:
    print("La cadena vacía es False")

if []:
    print("cierto")
else:
    print("La lista vacía es False")
