archivo = open("Escribir.txt","r")
matriz = []

for linea in archivo:
	arreglo_v = linea.split(",")
	arreglo = []
	for j in range(len(arreglo_v)):
		numero_s = int(arreglo_v[j])
		arreglo.append(numero_s)
	matriz.append(arreglo)

numero_uno = int(input("Multiplica: "))
numero_dos = int(input("Por: "))

print ("El resultado es: "+ str(matriz[numero_uno][numero_dos]))