nota_lab = float(input("Digite a nota do Trabalho de Laboratório: "))
print('')
nota_sem = float(input("Digite a nota da Avaliação Semestral: "))
print('')
nota_final = float(input("Digite a nota do Exame Final: "))
print('')
peso_lab = 2
peso_sem = 3
peso_final = 5
media = (nota_lab * peso_lab + nota_sem * peso_sem + nota_final * peso_final) / (peso_lab + peso_sem + peso_final)
if media >= 8.0:
    conceito = 'A'
elif media >= 7.0:
    conceito = 'B'
elif media >= 6.0:
    conceito = 'C'
elif media >= 5.0:
    conceito = 'D'
else:
    conceito = 'E'
print(f"A média ponderada é {media:.1f} e o conceito é {conceito}.")