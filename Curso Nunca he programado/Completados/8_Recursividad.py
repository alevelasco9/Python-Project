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