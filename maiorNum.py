lista_num = []
n1 = input("primeiro numero")
lista_num.append(int(n1))
n2 = input("segundo numero")
lista_num.append(int(n2))
n3 = input("terceiro numero")
lista_num.append(int(n3))

maiorNumero = lista_num[0]

if(maiorNumero < lista_num[1]):
    maiorNumero = lista_num[1]

if(maiorNumero < lista_num[2]):
    maiorNumero = lista_num[2]

print(maiorNumero)