print('Bem vindo a Hortifruti do Victor')
list = ['Banana - R$12Kg', 'Melão - R$10Kg', 'Uva - R$2Kg', 'Maçã - R$6Kg','Morango - R$4Kg', 'Pessego - R$7Kg']
Banana_Valor = int(12)
Melão_Valor = int(10)
Uva_Valor = int(2)
Maçã_Valor = int(6)
Morango_Valor = int(4)
Pessego_Valor = int(7)

print('Temos essa variedade de frutas!')
print(*list, sep="\n")

print('Quantas irá querer de cada uma?')
Banana_QTD = float(input('Quantos kg de Banana irá querer?(Obs: não coloque Kg, apenas o numero):'))
Melão_QTD = float(input('Quantos kg de Melão irá querer?(Obs: não coloque Kg, apenas o numero):'))
Uva_QTD = float(input('Quantos kg de Uva irá querer?(Obs: não coloque Kg, apenas o numero):'))
Maçã_QTD = float(input('Quantos kg de Maçã irá querer?(Obs: não coloque Kg, apenas o numero):'))
Morango_QTD = float(input('Quantos kg de Morango irá querer?(Obs: não coloque Kg, apenas o numero):'))
Pessego_QTD = float(input('Quantos kg de Pessego irá querer?(Obs: não coloque Kg, apenas o numero):'))

p_Banana = Banana_Valor * Banana_QTD
p_Melão = Melão_Valor * Melão_QTD
p_Uva = Uva_Valor * Uva_QTD
p_Maçã = Maçã_Valor * Maçã_QTD
p_Morango= Morango_Valor * Morango_QTD
p_Pessego = Pessego_Valor * Pessego_QTD
Soma = p_Banana + p_Melão + p_Uva + p_Maçã + p_Morango + p_Pessego
total_5 = float(Soma + (Soma * 0.05))

print('Compra Final:')
print(f'{Banana_QTD} Banana = {round(p_Banana,2)}\n {Melão_QTD} Melão = {round(p_Melão,2)}\n {Uva_QTD} Uva = {round(p_Uva,2)}\n {Maçã_QTD} Maçã = {round(p_Maçã,2)}\n {Morango_QTD} Morango = {round(p_Morango,2)}\n {Pessego_QTD} Pessego = {round(p_Pessego,2)} ')
print('------------------------------------------------')
print(f'Total = {round(total_5,2)} junto com 5% de entrega')



