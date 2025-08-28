class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __eq__(self, value): #magic method
        return self.name == value.name and self.color == value.color

    def __str__(self): #magic method 
        return (f"Name = {self.name}, Color = {self.color}")

    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")
bike1 = Bike("Yemaha R15", "Blue")
bike2 = Bike("Yamaha FZ", "Red")
# print(bike1.display())
print(bike1)
print(bike1==bike2)


