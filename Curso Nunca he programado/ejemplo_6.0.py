arreglo = [10,3,7,9,23,2]

suma = 0

for x in range(len(arreglo)):
	suma = suma + arreglo[x]

print "la suma de todas tus calificaciones es: "+ str(suma)

promedio = float(suma) / len(arreglo)

print "y el promedio de tus calificaciones es: "+ str(promedio)
	
