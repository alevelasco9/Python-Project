archivo = open("Archivo.txt","r")
matriz = []

for linea in archivo:
	arreglo_v = linea.split(",")
	arreglo = []
	for j in range(len(arreglo_v)):
		numero_s = int(arreglo_v[j])
		arreglo.append(numero_s)
	print arreglo
	matriz.append(arreglo)
print ""
numero_uno = int(raw_input("Multiplica: "))
numero_dos = int(raw_input("Por: "))

print "El resultado es: "+ str(matriz[numero_uno][numero_dos])