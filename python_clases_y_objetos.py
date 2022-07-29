"""
Autor: German Correa

Clases y Objetos.

 Un objeto es una entidad que agrupa un estado y una funcionalidad relacionadas. El estado del objeto se define a través de variables llamadas 
atributos, mientras que la funcionalidad se modela a través de funciones a las que se les conoce con el nombrede métodos del objeto.
Un ejemplo de objeto podría ser un coche, en el que tendríamos atributos como la marca, el número de puertas o el tipo de carburante y
métodos como arrancar y parar. O bien cualquier otra combinación de atributos y métodos según lo que fuera relevante para nuestro 
programa.

Una clase, por otro lado, no es más que una plantilla genérica a partir de la cuál instanciar los objetos; plantilla que es la que 
define qué atributos y métodos tendrán los objetos de esa clase.

Volviendo a nuestro ejemplo: en el mundo real existe un conjunto de objetos a los que llamamos coches y que tienen un conjunto de 
atributos comunes y un comportamiento común, esto es a lo que llamamos clase. 
Sin embargo, mi coche no es igual que el coche de mi vecino, y aunque pertenecen a la misma clase de objetos, son objetos distintos.

class Coche:

    def __init__(self, gasolina):
        self.gasolina = gasolina
    print “Tenemos”, gasolina, “litros”

    def arrancar(self):
        if self.gasolina > 0:
            print “Arranca”
        else:
            print “No arranca”

    def conducir(self):
        if self.gasolina > 0:
        self.gasolina -= 1
        print “Quedan”, self.gasolina, “litros”
    else:
        print “No se mueve”



"""