calificacion = 0
calificaciones = []
x = 1

def agregar_calificacion(arreglo, elemento):
	if elemento >= 0:
		arreglo.append(elemento)


print "muestra una calificacion negativa para mostrar todas las calificaciones."
print ""
while calificacion >= 0:
	calificacion = float(raw_input("Dame la "+ str(x)+ " calificacion: "))
	agregar_calificacion(calificaciones,calificacion)
	x = x+1
print ""
print calificaciones
print ""
suma = 0

for cal in calificaciones:
	suma = suma + cal
print "El promedio de tus calificaciones es: "+ str(float(suma/len(calificaciones)))