import sys
import time

def efeito_digitacao(texto, delay=0.05):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
efeito_digitacao('Bem-Vindo ao Gym Control!', delay=0.05)
efeito_digitacao('Aqui você pode controlar seus treinos e acompanhar seu progresso.')
nome = input('Por favor, insira seu nome: ')
efeito_digitacao(f'Olá, {nome}! Vamos começar a configurar seu perfil de treino.')
idade = input('Insira sua idade: ')
peso = input('Insira seu peso (em kg): ')
altura = input('Insira sua altura (em cm): ')
efeito_digitacao('Perfil criado com sucesso!')

IMC = float(peso) / ((float(altura)/100) ** 2)
efeito_digitacao(f'Seu IMC é: {IMC:.2f}')

if IMC < 18.5:
    print('Você está abaixo do peso ideal.')    
elif 18.5 <= IMC < 24.9:
    efeito_digitacao('Você está com o peso ideal.')
elif 24.9 <= IMC < 29.9:
    efeito_digitacao('Você está com sobrepeso.')
elif 29.9 <= IMC < 34.9:
    efeito_digitacao('Você está com obesidade grau 1.')
elif 34.9 <= IMC < 39.9:
    efeito_digitacao('Você está com obesidade grau 2.')
else:
    efeito_digitacao('Você está com obesidade grau 3.')

efeito_digitacao('Agora, vamos configurar seu plano de treino.')
objetivo = input('Qual é o seu objetivo principal? (emagrecimento, ganho de massa, manutenção corporal):')
dias_por_semana = int(input('Quantos dias por semana você pretende treinar?: '))
efeito_digitacao(f'Plano de treino configurado para {dias_por_semana} dias por semana com o objetivo de {objetivo}.')

if dias_por_semana >= 4:
    efeito_digitacao('Ótimo! Com essa frequência, você verá resultados significativos em pouco tempo.')
else:
    efeito_digitacao('Considere aumentar a frequência para melhores resultados. Vamos colocar como base 4 dias por semana.')
    dias_por_semana = 4
    efeito_digitacao('Aqui está um plano de treino sugerido para você:')
if objetivo.lower() == 'emagrecimento':
    efeito_digitacao('Segunda: Cardio(40m) + Treino/Musculação(Peito e Triceps - Supino reto 12x10x10x10, Supino Inclinado 12x10x10x8, Croos - Over 12x10x10, triceps testa 10x10x8, triceps corda 10x10x8) \nTerça - Feira:Treino/Musculação(Perna - Extensora 12x10x10,abdutora 12x10x10x10, agachamento livre 12x10x10, mesa flexora 10x10x10,cadeira flexora 10x10x10, panturrilha no smith até a) - Cardio ou Aerobico(40m - 60m)\nQuinta - Feira:Cardio(40m) \nSexta - Feira: Cardio + Treino/Musculação(Costas e Biceps - Pulley frente 10x10x10,remada livre 12x12x10, cerrote 10x10x10, pulldown 10x10x10, mesa romana 10x10x10,banco romano 10x10x10,rosca alternada 12x12x10)\n')
elif objetivo.lower() == 'ganho de massa':
    efeito_digitacao('Segunda: Treino/Musculação - Peito e Tríceps \nTerça - Feira: Treino/Musculação - Costas e Bíceps \nQuarta - Feira: Descanso \nQuinta - Feira: Treino/Musculação - Pernas e Ombros \nSexta - Feira: Treino/Musculação - Abdômen e Cardio(40m) \n')
else:
    efeito_digitacao('Segunda: Treino/Musculação - Corpo Inteiro \nTerça - Feira: Descanso \nQuarta - Feira: Treino/Musculação - Corpo Inteiro \nQuinta - Feira: Descanso \nSexta - Feira: Treino/Musculação - Corpo Inteiro \n')

efeito_digitacao('Lembre-se de sempre consultar um profissional de educação física antes de iniciar qualquer programa de treino.')
efeito_digitacao('Temos os seguintes planos mensais disponíveis:Bronze - R$50,00\n Prata - R$80,00\n Ouro - R$120,00\n Platina - R$200,00')
plano = input('Escolha um plano para assinar: ')
efeito_digitacao(f'Você escolheu o plano {plano}. Obrigado por assinar nosso serviço!')
pagamento = input('Qual será a forma de pagamento? (cartão de crédito, boleto, pix?)')
efeito_digitacao(f'Pagamento via {pagamento} selecionado. Processando pagamento...')
efeito_digitacao('...............',delay = 1)
efeito_digitacao('Pagamento realizado com sucesso! Bem-vindo ao Gym Control Premium!')

efeito_digitacao('Em breve, mais funcionalidades estarão disponíveis!')
efeito_digitacao('Obrigado por usar o Gym Control!')