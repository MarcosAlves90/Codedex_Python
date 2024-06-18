# Write code below 💖

guess = 0

tries = 0

while guess != 6 and tries != 5:
  guess = int(input("Adivinhe o número: "))
  tries += 1

if tries == 5:
  print("\nVocê perdeu!")
else:
  print("\nVocê venceu!")