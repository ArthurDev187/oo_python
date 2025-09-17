class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        
    def __str__(self):
        return f"Brand: {self.brand}; Model: {self.model}; Color: {self.color}; Year: {self.year}"
    
    
    
car_1 = Car(brand='Hiunday', year=2013, color='Black', model='i30')
print(car_1)
print()

car_1.color = 'Red'
print(car_1)