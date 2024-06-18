# Write code below 💖

hamburger = ["Nenhum", "Big Mac", "Quarteirão", "Cheeseburger", "McChicken", "McFish"]
bebida = ["Nenhum", "Coca-Cola", "Fanta", "Sprite", "Guaraná", "Água"]
acompanhamento = ["Nenhum", "Batata Frita", "Nuggets", "McFritas", "Onion Rings", "Salada"]
sobremesa = ["Nenhum", "McFlurry", "Sunday", "Casquinha", "Torta de Maçã", "Torta de Banana", "Cookie"]
pedido = []

def line(x):
    print("=="+"="*len(x))
    print(" " + x + " ")
    print("=="+"="*len(x))

def welcome():
    line("MENU DO MCDONALD'S")
    print("Faça seu pedido aqui!")
    
def get_input():
    x = int(input("\nResposta: "))
    pedido.append(x)

def get_item():
    print("\nHambúrgueres:\n")
    for i, item in enumerate(hamburger, 1):
        print(str(i) + " - " + item)
    get_input()
    print("\nBebidas:\n")
    for i, item in enumerate(bebida, 1):
        print(str(i) + " - " + item)
    get_input()
    print("\nAcompanhamentos:\n")
    for i, item in enumerate(acompanhamento, 1):
        print(str(i) + " - " + item)
    get_input()
    print("\nSobremesas:\n")
    for i, item in enumerate(sobremesa, 1):
        print(str(i) + " - " + item)
    get_input()

    return hamburger[pedido[0]-1], bebida[pedido[1]-1], acompanhamento[pedido[2]-1], sobremesa[pedido[3]-1]

def print_order(*order):
    print()
    line("RESUMO DO PEDIDO")
    print("\nHambúrguer:", order[0])
    print("Bebida:", order[1])
    print("Acompanhamento:", order[2])
    print("Sobremesa:", order[3])

welcome()

print_order(*get_item())
