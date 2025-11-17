
print('Bem vindo a interface da Microsoft para aquisição da assinatura GamaPass')

assinatura = int(119)
nome = input('Digite seu nome:')
idade = input('Sua Idade:')
valor = int(input('Quanto o será feito de entrada?:'))
valor_assi = int(valor/assinatura)

if valor_assi > 1:
    print(f'Será adquirido {valor_assi} mêses de GamePass')
else:
    print('Senhor não deu entrada o suficiente')





