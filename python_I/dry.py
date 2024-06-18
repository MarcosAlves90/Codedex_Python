# Write code below 💖

# dry.py

# ----------------------

# A função len() retorna o número de items de um objeto.

ben_10 = ['Chama', 'Besta', 'Diamante', 'XLR8', 'Massa Cinzenta', 'Quatro Braços', 'Insectóide', 'Aquático', 'Ultra T', 'Fantasmático']

ben_10 = sorted(ben_10)

print(f"O ben 10 clássico tem: {len(ben_10)} aliens.")

# A função range() retorna uma sequência de números imutáveis.

# A função print() retorna mensagens ou valores na saída do programa.

print("\nOs aliens do ben 10 clássico são:\n")

for i in range(0,10):
    print(ben_10[0+i])

# A função max() retorna o maior item em um iterável ou em dois ou mais argumentos.

print(f"\nO único alien do ben 10 clássico que tem números no nome é o {max(ben_10)}.\n")

# ----------------------

# A função any() retorna True se pelo menos um elemento de um iterável for verdadeiro.

contem_a = any("a" in nome for nome in ben_10)

if contem_a:
    print("Pelo menos um dos aliens do ben 10 tem 'a' no nome.")
else:
    print("Nenhum dos aliens do ben 10 tem 'a' no nome.")