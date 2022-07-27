"""
Autor: German Correa

Explicando flujos de control en python.

Control de Flujo.

Se llama flujo de control al orden en el que se ejecutan las instrucciones de un programa, siendo las propias instrucciones las 
que determinan o controla dicho flujo.

En un programa, a menos que el flujo de control se vea modificado por una instrucción de control las instrucciones siempre 
se ejecutan secuencialmente, una detrás de otra, en orden de aparición, de izquierda a derecha y de arriba abajo, que es el 
flujo natural de un programa.

Para controlar el flujo se usa.

● Estructuras de control de flujo

- De selección

- Iterativas

● Lógica y valores de verdad

Estructuras de control de flujo de selección.
Deciden “el camino” a seguir entre dos o mas opciones
y siempre evalúan una expresión booleana para tomar
una decisión.

Tipos:

● Simple

La calificación de un alumno.

Para aprobar tiene que sacar 6.

La condicion es para aprobar la nota tiene que ser >=6

aprobar = 6

if aprobar == >=6:
    print("El alumno aprobo")

● Doble

La calificación de un alumno.

Para aprobar tiene que sacar 6. Caso contrario desaprueba

La condicion es para aprobar la nota tiene que ser >=6

aprobar = 6

if aprobar == >=6:
    print("El alumno aprobo")

else:
    print("El alumno desaprobo")

● Múltiple

La calificación de un alumno.

Para aprobar tiene que sacar 6. 

Si el alumno saca <6 y >=4 tiene recuperatorio.

Si el alumno saca <4 desaprueba

La condicion es para aprobar la nota tiene que ser >=6

aprobar = 6

if aprobar == >=6:
    print("El alumno aprobo.")

elif aprobar == >=4:
    print("El alumno va al recuperatorio.")

else:
    print("El alumno desaprobo la materia.")
"""

print("\nPrograma para saber si el alumno aprobo la materia o va al recuperatorio.")

nota = int(input("\nIngrese la nota del alumno: "))

aprob = 6

rec = 4

desap = 3

if nota  >=6:
    print("\nEl alumno aprobo la materia.\n")

elif nota >=4:
    print("\nEl alumno va al recuperatorio.\n")

else:
    print("\nEl alumno no aprobo la materia.\n")