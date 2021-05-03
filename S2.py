#Alexis Fuentes 40601
print("Ingrese el precio del producto")
precio= int(input())

print("ingrese el pago")
pago= int(input())

feria = pago - precio

def cambio(Billete):
    if pago< precio or Billete <0: 
        print("Valor invalido")
    else:
        Bd= Billete // 100
        Bc= Billete % 100 // 50              
        Bv= Billete % 100 % 50 //20      
        Md = Billete %100 % 50 % 20 //10                                     
        Mc =Billete %100 % 50 % 20 % 10 // 5 
        Mds = Billete %100 % 50 % 20 % 10 % 5 // 2 
        Mdu= Billete%100 % 50 % 20 % 10 % 5 % 2 // 1          
        print("Su cambio es",feria)
        print("Billetes de 100 ",Bd)
        print("Billetes de 50 ",Bc)
        print("Billetes de 20 ",Bv)
        print("Monedas de 10",Md)
        print("Monedas de 5 ",Mc)
        print('Monedas de 2',Mds)
        print("Monedas de 1 ",Mdu)

print(cambio(feria))


