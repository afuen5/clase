print('costo del producto: ')
costo = int(input())
print('Cuanto pagó ')
pago = int(input())

Sobra = pago - costo

if Sobra < 0:
	print("Cantidad insuficiente ")
else:
	Bd= Billete // 200
	Bc= Billete % 200 // 100              
	Bv= Billete % 200 % 100 //20      
	Md = Billete %200 % 100 % 20 //10                                     
	Mc =Billete %200 % 100 % 20 % 10 // 5 
	Mds = Billete %200 % 100 % 20 % 10 % 5 // 2 


	print("Su cambio es",feria)
	print("Billetes de 200 ",Bd)
	print("Billetes de 100 ",Bc)
	print("Billetes de 20 ",Bv)
	print("Monedas de 10",Md)
	print("Monedas de 5 ",Mc)
	print('Monedas de 2',Mds)

print(cambio(feria))