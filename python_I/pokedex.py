# Write code below 💖

class pokemon:
    def __init__(self,entry,name,types,description,is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    
    def speak(self):
        print(f"{self.name} {self.name}!")
    
    def display_details(self):
        print(f"Entry number: {self.entry}\nName: {self.name}\nType: {self.types[0] if len(self.types) == 1 else self.types[0] + '/' + self.types[1]}\nDescription: {self.description}\n{self.name + ' has already been caught!' if self.is_caught else self.name + ' hasn\'t been caught yet.'}")

pikachu = pokemon(25,'Pikachu',['Electric'],'Pikachu is an Electric-type Pokémon. Pikachu is able to generate electric charges, which it uses to shock its enemies or to recharge its own body.',True)
charmander = pokemon(4, 'Charmander', ['Fire'], 'Charmander is a Fire-type Pokémon. Charmander can breathe fire of such great heat that it melts anything. However, it never turns its fiery breath on any opponent weaker than itself.', False)
bulbasaur = pokemon(1, 'Bulbasaur', ['Grass','Poison'], 'Bulbasaur is a Grass/Poison-type Pokémon. Bulbasaur can be seen napping in bright sunlight. By soaking up the sun’s rays, the seed on its back grows progressively larger.', True)

pikachu.display_details()
pikachu.speak()
print()
charmander.display_details()
charmander.speak()
print()
bulbasaur.display_details()
bulbasaur.speak()