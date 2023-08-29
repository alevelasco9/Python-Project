calificacion = 0
calificaciones = []
x = 1
print ("muestra una calificacion negativa para mostrar todas las calificaciones.")
print ("")
while calificacion >= 0:
	calificacion = float(input("Dame la "+ str(x)+ " calificacion: "))
	if calificacion >= 0:
		calificaciones.append(calificacion)
	x = x+1
print ("")
print (calificaciones)
print ("")
suma = 0

for cal in calificaciones:
	suma = suma + cal
print ("El promedio de tus calificaciones es: "+ str(float(suma/len(calificaciones))))
print ("")
print ("")
print ("")
calificacion = 0
calificaciones = []
x = 1
print ("muestra una calificacion negativa para mostrar todas las calificaciones.")
print ("")
while calificacion >= 0:
	calificacion = int(input("Dame la "+ str(x)+ " calificacion: "))
	if calificacion >= 0:
		calificaciones.append(calificacion)
	x = x+1
print ("")
print (calificaciones)
print ("")
suma = 0

for cal in calificaciones:
	suma = suma + cal
print ("El promedio de tus calificaciones es: "+ str(suma/len(calificaciones)))