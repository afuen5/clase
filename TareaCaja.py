#Alexis Fuentes 40601
Pres = float(input("Ingrese el Precio del Articulo: "))
Pag = float(input("Con Cuanto Pagó?: "))

cambio = Pag - Pres
faltante = Pres - Pag

def caja(Billete):
	if(cambio>0):
		Bd= Billete // 100
		Bc= Billete % 100 // 50              
		Bv= Billete % 100 % 50 //20      
		Md = Billete %100 % 50 % 20 //10                                     
		Mc =Billete %100 % 50 % 20 % 10 // 5 
		Mds = Billete %100 % 50 % 20 % 10 % 5 // 2 
		Mdu= Billete%100 % 50 % 20 % 10 % 5 % 2
		print("Billetes de 100 ",Bd)
		print("Billetes de 50 ",Bc)
		print("Billetes de 20 ",Bv)
		print("Monedas de 10",Md)
		print("Monedas de 5 ",Mc)
		print('Monedas de 2',Mds)
		print("Monedas de 1 ",Mdu)
	elif(cambio==0):
		print("No ay Cambio, Gracias por su Compra")
	if (cambio < 0):
		print("Te Faltan ",str(faltante)+ " pesos")

print(caja(cambio))
