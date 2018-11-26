#Arreglo
lista = []
numero1 = int(input("Ingrese un numero 1 "))
numero2 = int(input("Ingrese un numero 2 "))
numero3 = int(input("Ingrese un numero 3 "))
numero4 = int(input("Ingrese un numero 4 "))
numero5 = int(input("Ingrese un numero 5 "))

lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
lista.append(numero4)
lista.append(numero5)
print(lista)


def menor_numero_arreglo () :
    menor = lista[0]
    for i in range (len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            
    print(menor)
        
    

menor_numero_arreglo()



