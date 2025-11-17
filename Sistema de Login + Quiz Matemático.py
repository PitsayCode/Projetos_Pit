import time
import sys

def efeito_digitacao(texto, delay=0.1):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def efeito_digitacao1(texto, delay=0.1):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
def efeito_digitacao2(texto, delay=0.1):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
efeito_digitacao("=== LOGIN ===", 0.2)
efeito_digitacao1("usuario:", 0.2)
Usuario = input()
efeito_digitacao2("Senha:", 0.2)
Senha = input()

efeito_digitacao1("Coloque novamente usuario:", 0.2)
Usuario1 = input()
efeito_digitacao2("Coloque novamente Senha:", 0.2)
Senha1 = input()

while Usuario != Usuario1 or Senha != Senha1:
    print("Usuário ou senha incorretos. Tente novamente.")
    efeito_digitacao1("Usuário: ", 0.2)
    Usuario1 = input()
    efeito_digitacao2("Senha: ", 0.2)
    Senha1 = input()

print("Login bem-sucedido!")

efeito_digitacao("=== QUIZ MATEMÁTICO ===", 0.1)
Teste = False
while Teste == False:
    Pergunta1 = 4
    pergunta2 = 15
    pergunta3 = 3
    respostas_certas = [4,15,3]
    respostas = []

    Resposta1 = int(input("Pergunta 1: Quanto é 2 + 2?: \n")) 

    if Resposta1 == Pergunta1:
        print('Certo')
        respostas.append(Resposta1)
    else:
        print('Errado')

    Resposta2 = int(input("Pergunta 2: Quanto é 5 * 3?: \n")) 

    if Resposta2 == pergunta2:
        print('Certo')
        respostas.append(Resposta2)
    else:
        print('Errado')

    Resposta3 = int(input("Pergunta 3: Qual a raiz quadrada de 9?: \n")) 

    if Resposta3 == pergunta3:
        print('Certo')
        respostas.append(Resposta3)
    else:
        print('Errado')
     
    if respostas == respostas_certas:
        Teste = True
    else:
        Teste = False

print("Chegou ao fim do teste")
    
    
