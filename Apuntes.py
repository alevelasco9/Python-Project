Apuntes = """

Funciones
	
	-print "lo que se quiera mostrar"													#Esta funcion es usada para mostrar la sentencia en pantalla.
	-input("Datos que solicite: ")														#Esta funcion es usada como una entrada de datos.
	-continue																			#Operador que permite repetir las iteracciones hasta que la condicion logica sea falsa.
	-open("Nombre del archivo.extension","permisos que se le otorga a la instruccion") 	#Esta funcion permite abrir un archivo y en funcion de los permisos que le concedamos podremos (w)escribir y modificarlo o (r)solamente leer el archivo
	-"Variable del archivo a abrir".write("lo que quiera escribir en el archivo") 		#Esta funcion hace que se escriba en el archivo lo que hayamos escrito anteriormente en el codigo.
	
	Cadenas:
	
		-"texto_ejemplo".capitalize()				#Genera una nueva cadena en la que la primera letra retorna mayuscula.
		-"texto_ejemplo".swapcase()					#Convierte dentro de la cadena las letras minusculas en mayusculas y viceversa
		-"texto_ejemplo".upper()					#Dentro de la cadena pasa todas las letras a mayusculas.
		-"texto_ejemplo".lower()					#Dentro de la cadena pasa todas las letras a minusculas.
		-"texto_ejemplo".[isupper / islower]()		#Muestra si la cadena esta escrita en mayusculas o minusculas respectivamente con valores booleanos.
		-"texto_ejemplo".title()					#muestra la cadena con una fuente de titulo.
		-"Texto_ejemplo".replace("texto_1", "texto_2", "numero_reemplazos")			#En el "texto_1" define el texto que se quiere borrar y en el "texto_2" se define el texto que lo reemplaza y en "numero_reemplazos" introducimos un valor int indicando cuantas veces queremos que se repita.
		-"texto_ejemplo".strip()					#Elimina los espacios al principio y final de la cadena.
		-"Cadena {} ejemplo".format("Variable") 	#Utilizamos los corchetes para definir la zona de la cadena donde queremos añadir la variable, esta forma podemos nombrar a las variables para introducirlas en el orden deseado.
		-"Ejemplo cadena %s" %("variable")			#Utilizamos los %s para seleccionar la posicion de la variable dentro de la cadena.
		-"Variable".stratswith("elemento")			#Muestra si la cadena comienza con el elemento indicado reflejando un valor booleano.
		-"Variable".endswith("elemento")			#Muestra si la cadena acaba con el elemento indicado reflejando un valor booleano.

	Estructura de datos:
	
		Listas y tuplas:
			-Lista[Desde  :  Hasta  :  Numero de saltos ]						#El ":" es usado para seleccionar desde un elemento de la lista hasta otro marcado por su indice, si añadimos un segundo ":" podremos seleccionar los saltos que python va a dar al leer la lista.
			-len("recuento de valores dentro de una estructura de datos")		#Esta funcion se usa para contar el numero de valores que se encuentran dentro de "[]" de una estructura de datos.
			-"lista".append("Objeto añadido")									#Añade al final del lista el valor o expresion que elijamos.
			-"lista".insert(Posicion,"Objeto añadido")					#Añade en la posicion elegida el valor o expresion que queramos.
			-"lista".extend("lista_2")									#Se suman los elementos de ambos listas.
			-"lista".remove("Elemento a desechar")						#Elimina el elemento del lista.
			-"lista".pop("posicion del elemento")						#Elimina el elemento que exista en la posicion seleccionada.
			-"ejemplo_lista".split("elemento_excluido")					#Generamos una nueva lista con el elemento seleccionado excluido.
			-"elemento_incluido".join("ejemplo_lista")					#Incluimos un caracter separador en la lista.
			-"ejemplo_lista".splitlines()								#Generamos una nueva lista a partir de un texto con saltos de linea.
			-"lista".sort()							#Ordena la lista de forma creciente segun los valores de sus elementos.
			-"lista".sort(reverse=true)				#Ordena la lista de forma decreciente segun los valores de sus elementos.
			-min("lista")							#Mostrara el menor valor existente en la lista.
			-max("lista")							#Mostrara el mayor valor existente en la lista.
			-"Elemento" in "lista"					#Reflejara un valor booleano en el que mostrara si el elemento existe en la lista o variable nombrada.
			-"Variable".index("Elemento")			#Muestra en que lugar se encuentra el elemento..
			-"Variable".count("Elemento")			#Muestra el numero de veces que se repite el elemento.
			-"variable".find("Elemento")			#Muestra la posicion en la que se encuentra el elemento dentro de la variable.
			-tuple("estructura_ejemplo")			#Funcion usada para copiar una lista y pasarla a tupla.
			-list("estructura_ejemplo")				#Funcion usada para copiar una tupla y pasarla a lista
			-zip("ejemplo_1", "ejemplo_2")			#Funcion usada para comprimir otras listas o tuplas en una tupla.
			-EstructuraDatos.clear()				#Vacia completamente toda la estructura.

		Diccionarios:
			-diccionario["llave_1"] = "valor_1"					#Introduce una llave y su valor en el diccionario o en el caso de que ya exista la llave modificara su valor.
			-"Variable" = diccionario["llave_1"]				#Muestra el valor asignado a la llave.
			-diccionario.get("Key", "ejemplo")					#Muestra el valor asignado a la llave, se le puede añadir un segundo valor despues del elemento para reflejar el valor deseado en caso de que la llave no exista.
			-diccionario.setdefault("key", "Valor_ejemplo")		#Muestra el valor asignado a la llave, en caso de que no exista añadiria al diccionario la llave con el valor que se le asigne.
			-diccionario.keys()						#Muestra un objeto tipo "dict_keys(["a", "b", ...])" el cual nos muestra todos las llaves de un diccionario, se puede cambiar a tupla o lista si no se quiere trabajar con este objeto.
			-diccionario.values()					#Muestra un objeto tipo "dict_values(["a", "b", ...])" el cual nos muestra todos los valores de un diccionario, se puede cambiar a tupla o lista si no se quiere trabajar con este objeto.
			-diccionario.items()					#Muestra un objeto tipo "dict_items([("a", 1), ("b", 2), ...])" el cual nos muestra todos las llaves y sus valores dentro de un diccionario, se puede cambiar a tupla o lista si no se quiere trabajar con este objeto.
			-del diccionario["key"]					#El termino del es una palabra reservada. En este caso es usado para eliminar un key de un diccionario junto su valor.
			-diccionario.clear()					#Vacia completamente toda la estructura.

Tipados
	-int("numero")				#Tipado para determinar que los numeros son enteros.
	-float("numero")			#Tipado para determinar que los numeros son decimales.
	-str("valor numerico")		#Tipado usado para pasar numeros(valores) a cadena para que se puedan leer.



Conceptos
	
	Tipados:
		-Existen diferentes niveles de tipados que son asignados en funcion de necesitar mas o menos diferenciar los tipos
		 de datos que almacenan las variables. Tambien existen dos tipos de tipados que utilizan las variables dependiendo
		 de la flexibilidad que tengan el cambiarlas: tipados dinamicos y tipados estaticos.

	Variables:
		-Son contenedores de informacion que ocupan un espacio en la memoria. existen diferenter tipos de datos a 
		 guardar dentro de una variable y es necesario especidicarlo para saber cuanto espacio sera necesario reservar 
		 para la variable exceptuando lenguajes que usen un interprete que lo haga de forma automatica como en python.

	concatenacion
		-La concatenación es el proceso de anexar una cadena al final de otra cadena. Al concatenar literales o constantes 
		 de cadena mediante el operador +, el compilador crea una única cadena.

	Bloque identado
		-Linea de codigo escrita en un subloque en la que expresamos lo que sucedera acontinuacion, esto se escribira
		 usando siempre la tecla "TAB" o en su defecto usando la tecla "ESPACIO" manteniendo siempre la misma separacion
		 en todas las lineas.

	Ciclos
		-Instrucciones que se repiten definida o indefinidamente dependiendo de la necesidad del programa y siempre que
		 el resultado de la pregunta sea verdadero.

	Funciones
		-Conjunto de codigo comun definido que se llamara para evitar volver a escribir el mismo conjunto de codigo numerosas veces.

	Recursividad
		-Ciclo en el que una funcion se llama a si misma.



Operadores:

	1.1 Operadores aritmeticos:

		-Sumas -> "+"
		-Restas -> "-"
		-Multiplicacion -> "*"
		-Division -> "/"
		-Modulo -> "%"
		
	1.2 Orden de ejecion:

		1º- Negacion "¬"
		2º- Modulo "%" 
		3º- Exponenciacion "^"
		4º- Multiplicacion y division
		5º- Sumas y restas
		6º- Operadores logicos
	
	1.3 Operadores de variables:

		-Suma las variables. 		-> " += "
		-Resta las variables.		-> " -= "
		-Multiplica las variables. 	-> " *= "

	1.4 Operadores relacionales:

		-Mayor que: ">"
		-Menor que: "<"
		-Mayor o igual que: ">="
		-Menor o igual que: "<="
		-Igual que: "=="
		-Diferente que: "!="

	1.5 Operadores logicos:

		-and	#Es un operador logico en el que todas las operaciones deben de ser verdaderas para que el resultado final sea verdadero.
		-or  	#Es un operador logico en el que todas las operaciones deben de ser falsas para que el resultado final sea falso.
		-not 	#Es un operador logico el cual cambia el sentido del resultado. Ejemplo:  "variable" = not true --> "variable" = falso
		-is  	#Es un operador logico en el que las operaciones deben de resultar iguales para que el resultado final sea verdadero.



Condiciones:
	
	Realizar una toma de decisiones.
		-Usamos la instruccion "if" y posteriormente añadiremos la cuestion para valorar si es verdadera o falsa.
		 Si la cuestion resultase falsa debemos usar la instruccion "else" en el mismo bloque para determinar lo que pasara.
		
			Ejemplo: 
				if (condicion(cuestion)):
					consecuencia
				else:
					alternativa
					
		Nota: un condicional puede ser expresado de forma negativa expresandolo de la siguiente manera:
				if not (condicion)
					consecuencia
				else:
					alternativa


			
Ciclos:
	
	-for
		Tipo de ciclo al cual se le establece un rango dandole valores los cuales corresponden
		a las secuencias del ciclo.
		
			Ejemplo:
				for x in range(x(0),x(1))
					pass
					
	-while
		Tipo de ciclo en el que se escribe la condicion logica(pregunta) justo despues de escribir
		la instruccion while.
		
			Ejemplo:
				while x != y 
					pass
		
		

Estructura de datos:
	Son formas predefinidas de organizar la información y funcionan como una especie de variable que almacena mas de un valor separados por ",".

		-Listas
			Es una estructura de datos basica donde poder almacenar str, int, float, bool, listas... De forma que se ordenan en indices comenzando siempre por el 0 como el primer valor almacenado.
			Esta estructura de datos se puede manipular despues de definirla con sus correspondientes funciones pudiendo asi introducir o remover informacion dentro de la lista, esta estructura de
			datos tiene el inconveniente de que python lo lee mas lento frente a las Tuplas.

				Ejemplo:
					Ejemplo_lista = [valor_1, valor_2, ...]
		

		-Tuplas
			Es una estructura de datos donde almacenamos str, int, float, bool, lista, tupla... De forma ordenada con indices comenzando por el 0 como el primer valor almacenado.
			Esta estructura de datos se mantendra inmutable y no podra se modificada su informacion mediante codigo una vez definida, esta estructura de datos tiene la ventaja 
			de que python lo lee mas rapido frente a las listas.
				
				Ejemplo:
					Ejemplo_tupla = (valor_1, valor_2, ...)

		-Diccionarios
			Es una estructura de datos donde almacenamos str, int, float, bool, lista, tupla, diccionarios... Solo se puede acceder a los valores de los diccionarios a traves de
			llaves, las cuales deben ser variables inmutables. Esta estructura de datos es mutable por lo que se puede modificar sus valores y tamaño,

				Ejemplo:
					Ejemplo_diccionario = {"llave_1" : "valor_1", "llave_2":"valor_2", ...}


		-Arreglos(Listas en python)
			Es la estructura de datos mas basica de todas y en algunos lenguajes tradicionales como java y C solo admitiran arreglos de un solo tipo.
			Los valores estan ordenados en un orden de posicion establecido el cual comienza por 0.
			
				Ejemplo:
					arreglo = [2,5,3,6,3,6]
			
			Ademas se pueden modificar los valores que se encuentran dentro del arreglo expresandolo como en el siguiente ejemplo:
				
				 Ejemplo:
					arreglo = [2,5,3,6,3,6]
					
					arreglo[0] = 6 #Entonces el valor que mostraria no seria 2 sino que mostraria el valor 6








"""
archivos = open("apuntes.txt","w")
archivos.write(Apuntes)