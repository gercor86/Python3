"""
Auto: German Correa

Diccionarios.

Un diccionario es un conjunto de parejas clave- valor (key-value). Es decir, se accede a cada
elemento a partir de su clave. Se definen de la siguiente manera:

estudiante = {

"nombre": "Iñaki Perurena",

"edad": 30,

"nota_media": 7.25,

"repetidor" : False

}

Las claves tienen que ser únicas y estar formadas por un string o un número. Para acceder al
valor de una clave exiten dos maneras distintas:

edad = estudiante["edad"] # devuelve el valor de 'edad'

nota_media = estudiante.get("nota_media") # devuelve el valor de 'nota_media'


estudiante["edad"] = 25 # actualiza el valor de 'edad'

estudiante["suspensos"] = 3 # inserta una nueva pareja clave - valor

estudiante.update({'aprobados':'8'}): inserta una nueva pareja clave - valor o actualiza su valor si ya existiera.

Algunos de los métodos más utilizados son los siguientes:

Método
diccionario.keys()
diccionario.values()
diccionario.pop(clave[,<default>])
diccionario.clear()
diccionario.clear()
clave in diccionario
valor in diccionario.values()

Acción

Devuelve todas las claves del diccionario
Devuelve todos los valores del diccionario
Elimina la clave del diccionario y devuelve su valor asociado. Si no la encuentra y se indica un valor por defecto, devuelve el
valor por defecto indicado.

Vacía el diccionario

Devuelve True si el diccionario contiene la clave o False en caso contrario.


Diccionarios

Recorrer un diccionario

La forma más habitual de recorrer un diccionario es mediante la sentencia for. Al recorrer un
diccionario, por defecto se iterará sobre sus claves:

diccionario = {'a':1, 'b':2,'c':3}

for key in diccionario:

print(key)


# Resultado: a b c

Es decir, el código anteiror será equivalente al siguiente:

diccionario = {'a':1, 'b':2,'c':3}

for key in diccionario.keys():

print key

# Resultado: a b c
Por lo tanto, para iterar accediendo a los valores, realizaremos lo siguiente:

diccionario = {'a':1, 'b':2, 'c':3}

for key in diccionario:

print(diccionario[key])


# Resultado: 1 2 3

Otro manera alternativa sería empleando la función items(), la cual devuelve el diccionario como tuplas de tipo (key,value):

diccionario = {'a':1, 'b':2, 'c':3}

for key, value in diccionario.items():

print("El valor de %s is %d" % (key, value))


#Resultado:

#El valor de a is 1

#El valor de b is 2

#El valor de c is 3

Borrar un elemento

Para borrar un elemento de un diccionario se utiliza la instrucción del.

Diccionarios
 
edades = {"Ane":22,"Jokin": 27,"Aitor": 15}

del edades["Aitor"]

Otra alternativa también utilizada y mencionada anteriormente es la función pop(), el cual devuelve
el valor del elemento eliminado:

edades = {"Ane":22, "Jokin":27, "Aitor":15}

edades.pop("Aitor")

"""
