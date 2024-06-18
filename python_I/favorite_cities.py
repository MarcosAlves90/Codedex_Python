# Write code below 💖

class City:
    def __init__(self, name, country, population, landmarks, mayor, founding_year, gentilic):
        self.name = name
        self.country = country
        self.population = round(population / 1000) * 1000
        self.landmarks = landmarks
        self.mayor = mayor
        self.founding_year = founding_year
        self.gentilic = gentilic 

maua = City('Mauá','Brasil',477552,['Mauá Plaza Shopping','Parque Ecológico da Gruta Santa Luzia'],'Francisco Marcelo Oliveira',1954,'mauaense')
tokyo = City('Tokyo', 'Japan', 14094034, ['Tokyo Tower', 'Santuário Meiji'], 'Yuriko Koike', 1889, 'Tokyoite')

print(vars(maua))
print(vars(tokyo))