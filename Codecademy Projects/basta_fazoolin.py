class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"This franchise is location in {self.address}"

    def available_menus(self, time):
        for menu in self.menus:
            if time > menu.start_time and time < menu.end_time:
                print(menu.name)

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"The menu is {self.name}. It is available from {self.start_time} till {self.end_time}"

    def calculate_bill(self, purchased_items):
        total_bill = 0
        for item in purchased_items:
            total_bill += self.items[item]
        return total_bill

brunch_item = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
}

early_bird_item = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00,
}

dinner_item = {
  'crostini with eggplant caponata': 13.00, 
  'ceaser salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00
}

kids_item = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}

# Creating actual menus
brunch = Menu("Brunch", brunch_item, 1100, 1600)
early_bird = Menu("Early Bird", early_bird_item, 1500, 1800)
dinner = Menu("Dinner", dinner_item, 1700, 2300)
kids = Menu("Kids", kids_item, 1100, 2100)

brunch_first_order = brunch.calculate_bill(["pancakes", "home fries", "coffee"])
early_bird_first_order = early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])

# Creating our franchises
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

new_installment.available_menus(1700)