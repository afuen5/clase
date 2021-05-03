precio_articulo = float(input('Precio del Articulo: '))
monto_ingreso = float(input('Con Cuanto Pagó: '))


def caja(precio,monto):
	if(monto > precio):
		resta = monto - precio
		cinco = Moneda5(resta)
		diez = Moneda10(resta)
		veinte = Moneda20(resta)
		cincuenta= Moneda50(resta)
		cien= Moneda100(resta)
		return 'Tu cambio es de: '+str(resta)+'\nMonedas de 10: ' +str(diez)+' Monedas' + '\nMonedas de 5: '+str(cinco) +' Monedas'+'\nBillete/s de 20: '+str(veinte) +' Billete'+'\nBillete/s de 50: '+str(cincuenta) +' Billete'+'\nBillete/s de 100: '+str(cien) +' Billete'

	elif(monto == precio):
		return 'No cambio '
	else:
		return 'Te Falta Dinero'




def Moneda5(cambio):
	if(cambio<=5):
		return (int(cambio/5))
	else:
		return ('0')

def Moneda10(cambio):
	if(cambio<=20):
		return (int(cambio/10))
	else:
		return('0')
def Moneda20(cambio):
	if(cambio<=20):
		return (int(cambio/20))
	else:
		return('0')

def Moneda50(cambio):
	if(cambio<=20):
		return (int(cambio/50))
	else:
		return('0')

def Moneda100(cambio):
	if(cambio>):
		return (int(cambio/100))
	else:
		return('0')








	#return int(cambio/10)
#def Moneda5(cambio):
	#return int(cambio/5)

resultado = caja(precio_articulo, monto_ingreso)

print(resultado)