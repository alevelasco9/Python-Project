arreglo = [10,3,7,9,23,2]

suma = 0
print "Calificaciones: "+ str(arreglo)
print ""
for x in range(len(arreglo)):
	suma = suma + arreglo[x]

print "la suma de todas tus calificaciones es: "+ str(suma)

promedio = float(suma) / len(arreglo)

print "y el promedio de tus calificaciones es: "+ str(promedio)

print ""
print ""
print ""

publicaciones = ["comida en casa de mis padres","noche divertida con los amigos","gran fin de semana"]

print "Muro de red social."
print " "
for publicacion in publicaciones:
	print publicacion
	
print ""
print ""
print ""

frutas = ["fresas","mango","sandia","melon"]
verduras = ["lechuga","tomate","pimiento"]
print "Lista de verduras y futa"
print ""

verduras.extend(frutas)

frutas.append("uva")

frutas.insert(1,"manzana")

frutas.remove("melon")

frutas.pop(0)

print frutas
print ""
print verduras

print ""
print ""
print ""

calificacion = 0
calificaciones = []
x = 1
print "muestra una calificacion negativa para mostrar todas las calificaciones."
print ""
while calificacion >= 0:
	calificacion = float(raw_input("Dame la "+ str(x)+ " calificacion: "))
	if calificacion >= 0:
		calificaciones.append(calificacion)
	x = x+1
print ""
print calificaciones
print ""
suma = 0

for cal in calificaciones:
	suma = suma + cal
print "El promedio de tus calificaciones es: "+ str(float(suma/len(calificaciones)))
print ""
print ""
print ""
calificacion = 0
calificaciones = []
x = 1
print "muestra una calificacion negativa para mostrar todas las calificaciones."
print ""
while calificacion >= 0:
	calificacion = int(raw_input("Dame la "+ str(x)+ " calificacion: "))
	if calificacion >= 0:
		calificaciones.append(calificacion)
	x = x+1
print ""
print calificaciones
print ""
suma = 0

for cal in calificaciones:
	suma = suma + cal
print "El promedio de tus calificaciones es: "+ str(suma/len(calificaciones))