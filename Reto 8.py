class MenuItem:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    
    def total_price(self):
        return self.price 

class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

class Apetizer(MenuItem):
    def __init__(self, name, price, shared):
        super().__init__(name, price)
        self.shared = shared

class MainCourse(MenuItem):
    def __init__(self, name, price, vegetarian):
        super().__init__(name, price)
        self.vegetarian = vegetarian

# Clase Menu que implementa un iterable
class Menu:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)

    def show(self):
        print("MENU:")
        for item in self:
            print(f"- {item.name} (${item.price:.2f})")
            if isinstance(item, Beverage):
                print(f"  Type: Beverage | Size: {item.size}")
            elif isinstance(item, Apetizer):
                print(f"  Type: Apetizer | Shared: {item.shared}")
            elif isinstance(item, MainCourse):
                print(f"  Type: Main Course | Vegetarian: {item.vegetarian}")
            print("-" * 40)

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    def apply_discount(self):
        total = self.calculate_total()
        if len(self.items) > 6:
            return total * 0.8  # 20% de descuento
        return total

#----------------------

menu_items = [
    Beverage("Coke", 1.50, "Medium"),
    Beverage("Water", 1.00, "Large"),
    Beverage("Juice", 2.00, "Small"),
    Apetizer("Nachos", 5.00, True),
    Apetizer("Wings", 6.00, True),
    Apetizer("Fries", 3.00, False),
    MainCourse("Pasta", 12.00, True),
    MainCourse("Burger", 10.00, False),
    MainCourse("Steak", 15.00, False),
    MainCourse("Salad", 8.00, True),
]

# Crear menú iterable
menu = Menu(menu_items)

# Mostrar el menú
menu.show()

# Crear y usar una orden
order = Order()
order.add_item(menu_items[0])  # Coke
order.add_item(menu_items[2])  # Juice
order.add_item(menu_items[3])  # Nachos
order.add_item(menu_items[5])  # Fries
order.add_item(menu_items[6])  # Pasta
order.add_item(menu_items[8])  # Steak
order.add_item(menu_items[9])  # Salad

# Mostrar totales
print("Total before discount: $", order.calculate_total())
print("Total after discount: $", order.apply_discount())