#Cantidad de vueltas que da una rueda de 50 cm de diametro durante 1 km.
import math
vuelta = float((math.pi**2)*0.05)
vueltas_1km = float(1000*vuelta)
print ("El numero de vueltas que da una rueda en 1km es de: "+ str(vueltas_1km))