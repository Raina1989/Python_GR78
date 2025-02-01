class Car:
    def __init__(self, mileage, fuel_type, color, price):
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.color = color
        self.price = price

    def display_info(self):
        print(f"Car Information:")
        print(f"Mileage: {self.mileage} km/l")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Color: {self.color}")
        print(f"Price: ${self.price}")
# Creating an object of the Car class
my_car = Car(15, "Petrol", "Red", 15000)

# Calling a method on the object
my_car.display_info()
