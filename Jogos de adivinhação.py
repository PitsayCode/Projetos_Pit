import random
numero = random.randint(1,11)
palpites = []
tentativas = 0

print("Bem Vindo ao Jogo dos numeros")
usuario = input("Coloque aqui seu nome:")

palpite = int(input("Coloque aqui um numero:"))
palpites.append(palpite)

if palpite == numero:
    print("Caramba você acertou de primeira")
    print("Houve", tentativas, "tentativas e esses foram seus palpites", palpite)
else:
    while palpite != numero:
        print("Numero errado")
        tentativas += 1
        palpite = int(input("Tente de novo:"))
        palpites.append(palpite)
    



print("Você acertou", usuario , ",houve um total de", tentativas, "tentativas e esses foram seus palpites " + ", ".join(map(str, palpites)))