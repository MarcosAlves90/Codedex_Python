# Write code below 💖

import random

num = random.randint(1, 9)

pergunta = input("Digite sua pergunta: ")

print(f'\nQuestão: {pergunta}')

print('\nMagic 8 Ball:',end=' ')

if num == 1:
    print("Sim - Definitivamente.")
elif num == 2:
    print("É decididamente assim.")
elif num == 3:
    print("Sem sombra de dúvidas.")
elif num == 4:
    print("Resposta nebulosa, tente novamente.")
elif num == 5:
    print("Pergunte novamente mais tarde.")
elif num == 6:
    print("Melhor não te dizer agora.")
elif num == 7:
    print("Minhas fontes dizem que não.")
elif num == 8:
    print("A perspectiva não é tão boa.")
elif num == 9:
    print("Muito duvidoso.")