#Este programa muestra el promedio de 5 asignaturas cursadas por el usuario.
Español, Matematicas, Economia, Programacion, Ingles = int(input("Nota de Español: ")), int(input("Nota de Matematicas: ")), int(input("Nota de Economia: ")), int(input("Nota de Programacion: ")), int(input("Nota de Ingles: "))
Promedio = float((Economia+Español+Matematicas+Programacion+Ingles)/5)
print ("Tu nota de promedio es: "+ str(Promedio))