class Car:  # Define Car class
    def __init__(self, name, year):  # Initialize attributes
        self.name = name
        self.year = year
        
    def __str__(self):  # String representation
        return f"{self.name} ({self.year})"
    
    def checkYear(self):  # Check car model year
        if self.year <= 1999:
            print(f"This car {self.name} is an older model.")
        else:
            print(f"This car {self.name} is a newer model.")

car1 = Car("Toyota", 1992)  # Create Car object
car2 = Car("Nissan", 2008)  # Create Car object

print(car1.name)  # Print car1 name
print(car1.year)  # Print car1 year

car2.year = 2001  # Update car2 year
print(car1)  # Print car1 (calls __str__)

print(car1.checkYear())  # Call checkYear method
print(car2.checkYear())  # Call checkYear method

print(car2)  # Print car2 (calls __str__)
del car2  # Delete car2
print(car2)  # Error: car2 no longer exists
