class Trainer:
    def __init__(self, name, potions, pokemons):
        self.name = name
        self.potions = potions
        self.pokemons = pokemons
        self.current_pokemon = ""

    def set_current_pokemon(self, pokemon):
        if pokemon in self.pokemons and not pokemon.is_knocked_out:
            self.current_pokemon = pokemon
            print(f"{self.current_pokemon.name} is now your current pokemon")
        else:
            print(f"You either don't have {pokemon.name} or it has been knocked out")
    
    def use_potion(self, amount):
        if self.current_pokemon.health == self.current_pokemon.max_health:
            print(f"Your pokemon {self.current_pokemon.name} already is at max health")
        elif self.potions != 0:
            self.current_pokemon.regain_health(amount)
            self.potions -= 1
        else:
            print("You have zero potions")

    def attack(self, other):
        self.current_pokemon.attack(other.current_pokemon)
        print(f"{self.name} attacked {other.name}")

    def revive_pokemon(self, pokemon):
        if pokemon in self.pokemons and pokemon.is_knocked_out:
            pokemon.revive()

class Pokemon:
  def __init__(self, name, level, p_type, max_health):
    self.name = name
    self.level = level
    self.p_type = p_type
    self.max_health = max_health
    self.health = max_health
    self.is_knocked_out = False
    
  def lose_health(self, attacker, amount):
    if not self.is_knocked_out:
      self.health -= amount
      print(f"{attacker.name} attacked {self.name} and has dealt {amount}. Its current health is {self.health}")
      if self.health <= 0:
        self.knock_out()
  
  def regain_health(self, amount):
    if not self.is_knocked_out:
      self.health += amount
      print(f"{self.name} has gained health by {amount}. Its current health is {self.health}")
  
  def knock_out(self):
    self.is_knocked_out = True
    print(f"{self.name} has been knocked out")
  
  def revive(self):
    self.is_knocked_out = False
    self.health = self.max_health / 2
    print(f"{self.name} has been revived")
    
  def attack(self, other):
    # Working with Pokemon types
    # Advantageous Pokemon deal damage twice as much as their levels
    # Disadvantageous ones deal half the damage as their levels
    if self.p_type == "Fire" and other.p_type == "Grass":
        other.lose_health(self, self.level * 2)
    elif self.p_type == "Water" and other.p_type == "Fire":
        other.lose_health(self, self.level * 2)
    elif self.p_type == "Grass" and other.p_type == "Water":
        other.lose_health(self, self.level * 2)
    elif self.p_type == "Water" and other.p_type == "Grass":
        other.lose_health(self, self.level * (1/2))
    elif self.p_type == "Grass" and other.p_type == "Fire":
        other.lose_health(self, self.level * (1/2))
    elif self.p_type == "Fire" and other.p_type == "Water":
        other.lose_health(self, self.level * (1/2))

# Testing some pokemon and trainers
charmender = Pokemon("Charmender", 5, "Fire", 40)
piplup = Pokemon("Piplup", 4, "Water", 43)
bulbasaur = Pokemon("Bulbasaur", 5, "Grass", 64)
ninetails = Pokemon("Ninetails", 10, "Fire", 90)
squirtle = Pokemon("Squirtle", 8, "Water", 54)
oddish = Pokemon("Oddish", 3, "Grass", 30)

arafat = Trainer("Arafat", 3, [charmender, ninetails, oddish])
efaz = Trainer("Efaz", 2, [piplup, squirtle, bulbasaur])

# Let the games begin
# First attack Arafat
print("We are using Python eval() to evaluate any relevent command that you enter as input")
print("At first, it's you Arafat: ")

while True:
    eval(input())
