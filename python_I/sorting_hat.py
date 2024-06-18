# Write code below 💖

Grifinoria = 0
Corvinal = 0
LufaLufa = 0
Sonserina = 0

print("Você prefere o amanhecer ou o anoitecer?")
print("    1) Amanhecer\n    2) Anoitecer")

q1 = int(input("\nDigite sua resposta: "))

if q1 == 1:
  Grifinoria += 1
  Corvinal += 1
elif q1 == 2:
  LufaLufa += 1
  Sonserina += 1
else:
  print("\nEntrada inválida!")

print("\nQuando eu estiver morto, quero que as pessoas se lembrem de mim como:")
print("    1) O Bom\n    2) O Grandioso\n    3) O Sábio\n    4) O Corajoso")

q2 = int(input("\nDigite sua resposta: "))

if q2 == 1:
  LufaLufa += 2
elif q2 == 2:
  Sonserina += 2
elif q2 == 3:
  Corvinal += 2
elif q2 == 4:
  Grifinoria += 2
else:
  print("\nEntrada inválida!")

print("\nQual tipo de instrumento mais agrada os meus ouvidos?")
print("    1) O violino\n    2) O trompete\n    3) O piano\n    4) O tambor")

q3 = int(input("\nDigite sua resposta: "))

if q3 == 1:
  Sonserina += 4
elif q3 == 2:
  LufaLufa += 4
elif q3 == 3:
  Corvinal += 4
elif q3 == 4:
  Grifinoria += 4
else:
  print("\nEntrada inválida!")

if Grifinoria > Corvinal and Grifinoria > LufaLufa and Grifinoria > Sonserina:
  print("\nVocê será da Grifinória!")
elif Corvinal > LufaLufa and Corvinal > Sonserina:
  print("\nVocê será da Corvinal!")
elif LufaLufa > Sonserina:
  print("\nVocê será da Lufa-Lufa")
else:
  print("\nVocê será da Sonserina")