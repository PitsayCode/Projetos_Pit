def soma(*numero):
    resultado = 0
    for num in numero:
        print(f'{resultado} + {num} = {resultado + num}')
        resultado += num
    return f'O numero final é {resultado}'

x = soma(2, 3, 4, 7)
print(x)
