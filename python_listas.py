"""
Autor: German Correa

Listas.

Las listas en python son conjuntos de elementos ordenados y pueden estar conformadas por elementos de distintos tipos
(enteros, cadenas, float, funciones, lista).

Las listas en Python son mutables lo que significa que sus elementos pueden cambiar o reordenarse.

Las listas se delimitan por [] y sus elementos se separan por comas.

Los elementos pueden accederse mediente su indice.

Ejemplo.

lista_frutas = ["Banana", "Manzana", "Pera"]

Tambien puede contener otras listas dentro.

lista = ["jgf",["o", "u"], "casa", "cosa"]

Lista vacia.

mi_lista_vacia = []

Se puede crear lista vacias de dos formas.

lista_1 = []

lista = list()

Para saber las cantidad de elementos que tiene una lista se usa lo siguiente.

lista = ["Pizza", "Estofado"]

cantidad_elementos = len(lista)

print(cantidad_elementos)

Se puede acceder a los distintos elementos  de la lista por medio de su indice.

animales = ["Perro", "Gato", "Loro", "Conejo"]

print(animales[0])

El mensaje por pantalla sera "Perro".

Los indices de las listas empiezan por el 0, siguiendo asi contando hasta su totalidad. Si se usa numeros negativos, este ira en sentido
contrario de el ultimo elemento hasta el primer elemento.

Una lista anidada se considera como un solo elemento, independientemente de cuantos elementos contenga.

lista = ["CPU", "GPU", ["Ram", "HDD"], "Mouse", "Display"]


----------------------------------------------------------------------------------------------------------------------------------------

Modificar elementos de una lista.

Para modificar los elementos de una lista, indicando su posicion en la lista y dando un nuevo elemento.

mesa = ["Plato", "Tenedor", "Cuchara"]

mesa[0] = "Cuchillo"

----------------------------------------------------------------------------------------------------------------------------------------

Recorrer una lista.

Para recorrer una lista se utiliza en ciclo for usando range().

lista = ["pepe", "potasio", "calcio"]

for index in range (0, len(lista)):
    print(lista[index])

Tambien se puede usar.

lista = ["pepe", "potasio", "calcio"]

for elemento in lista:
    print(elemento)

-----------------------------------------------------------------------------------------------------------------------------------------

Agregar elementos a una lista

Para agregar elementos a una lista se usa el comando append()

lista_utiles =["Mochila", "Lapiz", "Birome"]

lista_utiles.append("Corrector")

Podemos agregar todos los elementos de otras listas  a una lista principal con el comando extend()

mi_lista_principal = ["mate", "yerba"]

mi_lista_dos = ["termo", "bombilla"]

mi_lista_pricipal.extend(mi_lista_dos)

print(mi_lista_pricipal)

-----------------------------------------------------------------------------------------------------------------------------------------

Obterner sublistas con (slicing)

Para obtener sublistas  se inicia desde una lista creada y luego se usa [:] de esta manera.

lista = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

lista_corta = lista[1:4]

print(lista_corta)

[2, 5]

El primer numero indica el indice del primer elemento, y el segundo en donde detenerse y dejar de tomar elementos.

-----------------------------------------------------------------------------------------------------------------------------------------

Ordenar una lista.

Para ordenar una lista podemos usar  el metodo sort()

num = [23, 54, 33, 12, 4, 6, 7, 1]

num.sort()

print(num)

[1, 4, 6, 7, 12, 23, 33, 54]

Para ordenar de forma inversa se usa el parametro reverse=True al metodo sort()

num.sort(reverse=True)

print(num)

[54, 33, 23, 12, 7 6, 4, 1]

Y invertir la lista se usa solo el metodo reverse()

num.reverse()

print(num)

[54, 33, 23, 12, 7 6, 4, 1]

----------------------------------------------------------------------------------------------------------------------------------------

Saber si un elemento se encuentra en la lista

para saber si un elemento se encuentra en la lista, podemos usar el operador in.

alumnos = ["Juan", "Lara", "Micaela", "Jorge"]
print("Lara" in alumnos)
True
print("Maria" in alumnos)
False
if "Micaela" in alumnos:
    print("se encuentra en la lista")

para saber cuantas veces se encuentra un elemento dentro de una lista podremos usar el método count()

numeros = [1, 4, 6, 3, 1, 1, 5, 6]

numeros.count(1)

3

numeros.count(6)

6

-----------------------------------------------------------------------------------------------------------------------------------------

Conocer el índice de un elemento

Podemos conocer el índice de un elemento utilizando el método index()

nombres = ["Mirian", "Sandra", "Walter", "Kevin", "Emilce"]

indice = nombres.index("Sandra")

print(indice)

1

print(nombres[indice])

Sandra

En caso de tener más de un elemento igual, index() solo va devolver el índice del primero.

lista = ["b", "a", "a","c","a"]

print(lista.index("a"))

1

-----------------------------------------------------------------------------------------------------------------------------------------

Eliminar elementos de una lista.

puedes eliminar elementos de una lista utilizando la palabra reservada del.

letras = ["a", "b", "c", "d", "e"]

print(letras)

["a", "b", "c", "d", "e"]

del letras[3]

print(letras)

["a", "b", "c", "e"]

en el ejemplo se borro "d" que se encontraba en el índice 3.

Podemos borrar de a varios elementos operando sublistas [:]

letras = ["a", "b", "c", "d", "e"]

del letras[2:5]

print(letras)

["a","b"]

Otra manera de eliminar elementos es con el método remove() y especificando el elemento a borrar.

palabras = ["hola", "casa", "zapatillas", "puerta", "tenedor"]

palabras.remove('casa')

print(palabras)

["hola", "zapatillas", "puerta", "tenedor"]

Otra forma de quitar elementos es utilizando el método pop(), que no sólo quitará un

elemento de la lista si no que nos retornará el valor quitado.

lista = ["mouse", "teclado", "monitor", "impresora"]

elemento_quitado = lista.pop()

print(elemento_quitado)

"impresora"

print("lista")

["mouse", "teclado", "monitor"]

También podemos especificar el índice del elemento que queremos quitar.

colores = ["amarillo", "verde", "azul", "rojo"]

color_quitado = lista.pop(2)

print(color_quitado)

"azul"

print(lista)

["amarillo", "verde", "rojo"]

Algunas funciones de python que puedes utilizar en listas son:

len() para saber la longitud(cantidad de elementos) que contiene una lista

min() devuelve el mínimo

max() devuelve el máximo

sum() devuelve la suma entre sus elementos

mi_lista = [1,2,3,4,5,6]

longitud = len(mi_lista)

print(longitud)

6

minimo = min(mi_lista)

print(minimo)

1

maximo = max(mi_lista)

print(maximo)

6

suma = sum(mi_lista)

print(suma)

21

También puedes utilizar operadores matemáticos en la listas

una_lista = ["a","b","c"]

otra_lista = [1, 2, 3]

resultado = una_lista + otra_lista

print(resultado)

["a","b","c",1,2,3]

animales = ["elefante", "leon", "tigre"]

print(animales)

["elefante", "leon", "tigre"]

animales += ["mono", "perro"]

print(animales)

["elefante", "leon", "tigre", "mono", "perro"]

resultado = una_lista * 3

print(resultado)

["a","b","c","a","b","c","a","b","c"]


"""

#print("Lista y usos.")

#objetos = ["Celular", "PC", "Escritorio", "Mouse"]

#objetos.sort()

#indice = objetos.index("PC")

#objetos.reverse()

#print(objetos)