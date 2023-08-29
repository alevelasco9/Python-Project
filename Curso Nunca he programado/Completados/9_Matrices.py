n = 11
n2 = 11
matriz = [[0 for i in range(n)] for j in range(n2)]

print matriz
print ""
print ""

for i in range(len(matriz)):
	arreglo = matriz[i]
	print arreglo
	
print ""
print ""

for i in range(len(matriz)):
	arreglo = matriz[i]
	for j in range(len(arreglo)):
		arreglo[j] = i * j
print matriz

print ""
print ""
		
numero_uno = int(raw_input("Multiplica: "))
numero_dos = int(raw_input("Por: "))

print "El resultado es: "+ str(matriz[numero_dos][numero_uno])