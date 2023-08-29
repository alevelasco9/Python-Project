#En esta actividad se muestra como resultado la altura de la sombra de un edificio de 20 metros en el que la luz del sol hace un angulo de 22 grados respecto al suelo.
import math

seno = (math.degrees(math.sin(22)))
hipotenusa = (20/seno)
altura_sombra = float(math.sqrt((hipotenusa**2)-(20**2)))
print (seno)
print ("")
print ("La altura de la sombra del edificio seria de: "+ str(altura_sombra)+ " metros.")