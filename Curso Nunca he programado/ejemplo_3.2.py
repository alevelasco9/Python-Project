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