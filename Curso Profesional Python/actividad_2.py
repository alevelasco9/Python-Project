#Esta actividad trata de mostrar al usuario la cantidad equivalente de dolares a euros.
euros_1 = float(0.86)
dolares_1 = float(1)
dolares_2 = float(input("Introduzca la cantidad en $ que quiera cambiar a €\n"))
euros_2 = ((dolares_2*euros_1)/dolares_1)
print ("la cantidad de "+ str(dolares_2)+ "$ es igual a "+ str(euros_2)+"€")