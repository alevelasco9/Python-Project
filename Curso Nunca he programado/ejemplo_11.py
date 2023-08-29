n = 1001
matriz = [[0 for i in range(n)] for j in range(n)]

for i in range(len(matriz)):
	arreglo = matriz[i]
	for j in range(len(arreglo)):
		arreglo[j] = i * j
		
archivo = open("Escribir.txt","w")

for i in range(len(matriz)):
	arreglo = matriz[i]
	for j in range(len(arreglo)):
		numero = arreglo[j]
		if j < (len(arreglo))-1:
			archivo.write(str(numero)+ ",")
		else:
			archivo.write(str(numero))
	if i < (len(matriz))-1:
		archivo.write("\n")