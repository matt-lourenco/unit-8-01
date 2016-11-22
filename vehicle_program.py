# Created on 22 Nov 2016
# Created by: Matthew Lourenco
# This is a program that creates a custom vehicle

from vehicle import *

#create a vehicle
car = Vehicle()
van = Vehicle()

print(car.current_state())
car.accelerate(100)
print(car.current_state())
car.brake(50)
print(car.current_state())

print(van.current_state())
van.accelerate(50)
print(van.current_state())
van.accelerate(160)
print(van.current_state())
