quantidade_livros = int(input("Digite a quantidade de livros que deseja comprar: "))
desconto_A = 0.25 * quantidade_livros + 7.50
desconto_B = 0.50 * quantidade_livros + 2.50
if desconto_A < desconto_B:
    print("A melhor opção de desconto é o critério A.")
else:
    print("A melhor opção de desconto é o critério B.")