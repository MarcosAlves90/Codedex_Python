# Write code below 💖

altura = float(input("Digite sua altura em centímetros: "))

creditos = int(input("\nDigite a quantidade de créditos: "))

if altura >= 137 and creditos >= 10:
    print("\nAproveite o passeio!")
elif altura < 137 and creditos >= 10:
    print("\nVocê não é alto o suficiente para andar neste brinquedo!")
elif altura >= 137 and creditos < 10:
    print("\nVocê não tem créditos o bastante para andar neste brinquedo!")
else:
    print("\nVocê não atende a nenhum dos requisitos para andar neste brinquedo!")