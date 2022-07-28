""" 
Autor: German Correa

Estructuras Repetitivas

Las estructuras que repiten una secuencia de instrucciones un número determinado de veces se denominan estructuras repetitivas,
iterativas o cíclicas.

Cada conjunto de instrucciones a ejecutar se denomina BUCLE. Y cada repetición del bucle se llama ITERACIÓN.

Todo bucle tiene que llevar asociada una condición, que es la que va a determinar cuándo se repite el bucle y cuándo deja de repetirse.

Contadores, Acumuladores y Banderas.

En muchos programas se necesitan variables que cuenten cuántas veces ha ocurrido algo (contadores), que indiquen si simplemente ha 
ocurrido un evento (banderas) o que acumulen valores (acumuladores).

Las situaciones pueden ser muy diversas, por lo que en este apartado simplemente se ofrecen unos ejemplos para entiendas 
cómo utilizar estos recursos:

* Contador

Los procesos repetitivos requieren contar los sucesos y acciones internas, una forma de hacerlo es mediante un contador.
Un contador es una variable cuyo valor se incrementa o decrementa en una cantidad constante en cada repetición.

* Acumulador

Un acumulador o totalizador es una variable cuya función es almacenar cantidades resultantes de operaciones sucesivas.
Realiza la misma función que un contador con la diferencia de que el incremento o decremento es variable en lugar de constante.

* Banderas

Una bandera, es una variable que puede tomar uno de dos valores (verdadero o falso) a lo largo de la ejecución del programa y 
permite comunicar información de una parte a otra del mismo.

Sentencia while (mientras)

Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla
una condición (es decir, mientras la condición tenga el valor True).
Queda en las manos del programador decidir el momento en que la condición cambie a False
para hacer que el ciclo While finalice.
Características:

● No se conoce la cantidad de veces a iterar o repetir el conjunto de acciones.

● El final del bucle está controlado con una condición.

● El conjunto de acciones se ejecutan mientras la evaluación de la condición devuelva un resultado verdadero.

● El ciclo se puede ejecutar 0 o más veces.

Ejemplo de codigo

Dado un número entero N calcular la suma de todos los números entre 1 y N.
cont = 0
suma = 0
N = int(input('Ingrese tope màximo: '))
while 
cont <= N:
suma = suma + cont
cont = cont + 1
print('La suma total es: ', suma)

Otra ventaja del bucle while es que el número de iteraciones no está definida antes de
empezar el bucle, por ejemplo porque los datos los proporciona el usuario.
Por ejemplo, el siguiente ejemplo pide un número positivo al usuario una y otra vez hasta que el
usuario lo haga correctamente:

Código

numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")


Sentencia for (para)

● Ahora SI se conoce la cantidad de veces a iterar o repetir el conjunto de acciones.

● El final de bucle está controlado un contador (indica cantidad de iteraciones). 

● La variable contador que maneja el bucle se incrementa automáticamente de acuerdo al incremento indicado.

● No necesita inicialización

La sintaxis de un bucle for es la siguiente:

Código

for variable in elemento iterable (lista, cadena, range, etc.):

Cuerpo del bucle

El cuerpo del bucle se ejecuta tantas veces como elementos tenga la estructura iterable(elementos de 
una lista o de un range(), caracteres de una cadena, etc.).

Utilizando tipos range()

Una las ventajas de utilizar tipos range() es que el argumento del tipo range() controla el número de veces que se 
ejecuta el bucle. Sirve para generar una lista de números que podemos recorrer fácilmente, pero 
no ocupa memoria porque se interpreta sobre la marcha:

Código

print("Comienzo")
for i in range(3):
    print("Hola ", end="")
print("Final")

Control de Bucles

Instrucción break.

Se puede usar en bucles for y while y simplemente termina el bucle actual y sigue con la ejecución de la próxima instrucción, por ejemplo:

a) Controlar fin de bucle

while True:
op = input('Ingrese cualquier palabra, termina con FIN--> ')
if op == 'FIN':
break
else:
print(op)
print('Terminó la ejecución con FIN')

b) La sentencia break es usada también para terminar un ciclo aun cuando la evaluación de la condición no devuelva False.

# Primer ejemplo

for letra in "Python":
if letra == "h":
break
print("Letra actual :", letra)

"""

print("\nContar hasta 10 con for.")

for n in range(1, 11):
    print("\n",n)

"""Con ciclo while"""

print("Cliclo While")

print("Bienvenido al Sistema")

usuario = "German"

contraseña = "1234"

int_u = input("Nombre de usuario: ")
int_c = input("Intraduzca la contraseña: ")

while int_u != usuario or int_c != contraseña:
    print("Usuario o contraseña incorrectos\n")
    int_u = input("Nombre de usuario: ")
    int_c = input("Intraduzca la contraseña: ")

else:
    print("\nAcceso Garantizado.\n")

print("Bienvenido al sistema.\n")