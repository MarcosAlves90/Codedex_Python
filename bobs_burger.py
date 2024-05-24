# Write code below 💖
 
# bobs_burgers.py
 
class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False
 
bobs_burgers = Restaurant()
mcdonalds = Restaurant()
n1_chicken = Restaurant()
 
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False
 
mcdonalds.name = 'McDonald\'s'
mcdonalds.category = 'Fast-food'
mcdonalds.rating = 4.3
mcdonalds.delivery = True

n1_chicken.name = 'N1 Chicken'
n1_chicken.category = 'Fast-food'
n1_chicken.rating = 4.7
n1_chicken.delivery = True

print(vars(bobs_burgers))
print(vars(mcdonalds))
print(vars(n1_chicken))