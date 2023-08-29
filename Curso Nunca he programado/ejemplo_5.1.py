nm = int(input("Dame el numero magico: "))
nnm = int(input("Introduce un numero: "))

while nm != nnm:
	if nm > nnm:
		nnm = int(input("Introduce un numero mayor: "))
		continue
	nnm = int(input("Introduce un numero menor: "))
print ("Lo lograste!")