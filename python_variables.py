# AUTOR: German Correa

# Las variables son unidad de almacenamiento y recuperacion de datos cona valores que pueden cambiar, la cual se identifica con un 
#  nombre unico en el codigo del programa.

# En python como muchos lenguajes modernos iran automaticamente liberando la memoria con un mecanismo llamado "recolector de basura".

edad = int(input("Ingrese su fecha de nacimiento", "Solo en números")) 

if edad >= 21:
	print("Eres mayor de edad")

elif edad == 18:
	print("Tu edad tiene reconocimientos de derechos pero no de decision propia")				

else:
	print("Eres menor de edad no puedes ingresar")