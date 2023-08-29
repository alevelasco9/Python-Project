nm = int(raw_input("Dame el numero magico: "))
nnm = int(raw_input("Introduce un numero: "))

while nm != nnm:
	if nm > nnm:
		nnm = int(raw_input("Introduce un numero mayor: "))
		continue
	nnm = int(raw_input("Introduce un numero menor: "))
print "Lo lograste!"