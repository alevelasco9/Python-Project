#Meses transcurridos desde tu fecha de nacimiento hasta la fecha actual.
Año_nacimiento_usuario = int(input("Introduce tu año de nacimiento: "))
año_actual = 2018
mes_actual = 9
años_transcurridos = (año_actual - Año_nacimiento_usuario)
meses_transcurridos = ((años_transcurridos*12)+mes_actual)
print ("Han transcurrido "+ str(meses_transcurridos)+ " meses desde tu nacimiento.")
print ("Han transcurrido "+ str(años_transcurridos)+ " años desde tu nacimiento.")

