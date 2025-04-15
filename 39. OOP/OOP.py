from car import Car

car_1 = Car("Chevy", "Corvette", 2021, 'red')
car_2 = Car("Ford", "Mustang", 2024, 'blue')

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()  

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()  