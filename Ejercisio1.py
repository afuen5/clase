
Nombres = []
n = int(input("cuantos nombres ingresara?\n"))
for i in range(n):
	nombre = input("ingrese el nombre numero " + str(i+1)+": ")
	nombres.append(nombre)
print(nombres)


print("print elemtento")
Nombres = reversed(Nombres)

for x in Nombres:
	print(x)
