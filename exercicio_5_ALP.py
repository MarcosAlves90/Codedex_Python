lista_produtos_nome = []
lista_produtos_valor = []
lista_produtos_quant = []
valor_total = 0.00
for i in range(1,6):
    texto1 = 'Qual o nome do produto '+str(i)+' ? '
    nome = input(texto1)
    texto2 = 'Qual o valor unitário do produto '+nome+' ? '
    texto3 = 'Qual a quantidade do produto '+nome+' ? '
    valor_un = float(input(texto2))
    quant = int(input(texto3))
    lista_produtos_nome.append(nome)
    lista_produtos_quant.append(quant)
    lista_produtos_valor.append(valor_un)
print('')
for i in range(0,5):
    print('Produto:',lista_produtos_nome[i],'Quantidade:',lista_produtos_quant[i],'Valor Unitário:',lista_produtos_valor[i],'Valor Total:',lista_produtos_valor[i]*lista_produtos_quant[i])   
    valor_total = valor_total + (lista_produtos_valor[i]*lista_produtos_quant[i])
print('')
print('O valor total de todos os produtos é:',valor_total)
print('')