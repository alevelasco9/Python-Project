#1º ejemplo

	print "Hola mundo!"


	
#2º ejemplo

	nombre = raw_input ("como te llamas: ")

	print ("Hola, encantado de conocerte "+ nombre + " yo me llamo alejandro")
	
	
	
#3º ejemplo

	#3.1
		N1 = raw_input ("Introduce un numero: ")
		N2 = raw_input ("Introduce otro numero: ")

		if N1 > N2:
			print (N1)+ " Es mayor que "+ (N2)
		else:
			print (N2)+ " Es mayor que "+ (N1)
			
	#3.2
		N1 = raw_input ("Introduce un numero: ")
		N2 = raw_input ("Introduce otro numero: ")
		N3 = raw_input ("Introduce otro numero: ")

		if N1 > N2:
			if N1 > N3:
				if N2 > N3:
					print (N1)+ " Es mayor que "+ (N2)+ " y "+ (N2)+ " Es mayor que "+ (N3)
				else:
					print (N1)+ " Es mayor que "+ (N3)+ " y "+ (N3)+ " Es mayor que "+ (N2)
			else:
				print (N3)+ " Es mayor que "+ (N1)+ " y "+ (N1)+ " Es mayor que "+ (N2)
		else:
			if N2 > N3:
				if N3 > N1:
					print (N2)+ " Es mayor que "+ (N3)+ " y "+ (N3)+ " Es mayor que "+ (N1)
				else:
					print (N2)+ " Es mayor que "+ (N1)+ " y "+ (N1)+ " Es mayor que "+ (N3)
			else: 
				print (N3)+ " Es mayor que "+ (N2)+ " y "+ (N2)+ " Es mayor que "+ (N1)
	

	
#4º ejemplo

	N = int(raw_input("Dame un numero: "))

	for x in range(0,11):
		print srt(x)+ " * "+ str(N)+ " = "+ str((N * x))



#5º ejemplo
print "5º ejemplo"

	#5.1
		nm = int(raw_input("Dame el numero magico: "))
		nnm = int(raw_input("Introduce un numero: "))

		while nm != nnm:
			if nm > nnm:
				nnm = int(raw_input("Introduce un numero mayor: "))
				continue
			nnm = int(raw_input("Introduce un numero menor: "))
		print "Lo lograste!"
		
	#5.2
		x = 0 
		while x < 40:
			x += 1
			if not x % 2 == 0:
				continue
			print x



#6ºejemplo

	#6.0
		arreglo = [10,3,7,9,23,2]

		suma = 0

		for x in range(len(arreglo)):
			suma = suma + arreglo[x]

		print "la suma de todas tus calificaciones es: "+ str(suma)

		promedio = float(suma) / len(arreglo)

		print "y el promedio de tus calificaciones es: "+ str(promedio)
		
		
	#6.1
	
		publicaciones = ["comida en casa de mis padres","noche divertida con los amigos","gran fin de semana"]

		print "Muro de red social."
		print " "
		for publicacion in publicaciones:
			print publicacion
			
			
	#6.2
	
		frutas = ["fresas","mango","sandia","melon"]
		verduras = ["lechuga","tomate","pimiento"]

		verduras.extend(frutas)

		frutas.append("uva")

		frutas.insert(1,"manzana")

		frutas.remove("melon")

		frutas.pop(0)


		print frutas
		print ""
		print verduras
	
	
	#6.3
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



#7º ejemplo

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



#8º ejemplo

	#En este ejemplo veremos como optimizar un programa usando la recursividad.

	from math import factorial
	n = int(raw_input("dame el numero: "))


	print ""
	def my_factorial(n):
		factorial_total = 1
		while n > 1:
			factorial_total *= n
			n -= 1
		return factorial_total
		
	print factorial(n)
	print my_factorial(n)


	print ""
	print "codigo optimizado con recursividad."
	print ""


	def mi_factorial(n):
		if n > 1:
			return n * mi_factorial(n-1)
		return 1
	print mi_factorial(n)
	
	
	
#9º ejemplo

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



#10º ejemplo

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



#11º ejemplo

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
