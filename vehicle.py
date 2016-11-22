# Created on 22 Nov 2016
# Created by: Matthew Lourenco
# This is a class that defines a generic vehicle

class Vehicle:
    #This is a class that creates a generic vehicle
    
    def __init__(self):
        #private fields
        
        self.__license_plate_number = 'AAAA000'
        self.__colour = 'white'
        self.__number_of_doors = 4
        self.__speed = 0
        self.__maximum_speed = 200
        self.__minimum_speed = -30
        self.__number_of_wheels = 4
        self.__number_of_tires = 4
    
    #public methods
    def accelerate(self, speed_increase):
        #increases the speed
        
        #if speed is less than max speed increase speed but do not increase over max speed
        if self.__speed < self.__maximum_speed:
            self.__speed = self.__speed + speed_increase
            if self.__speed > self.__maximum_speed:
                self.__speed = self.__maximum_speed
        else:
            print('Can not increase speed past maximum speed.')
    
    def brake(self, speed_decrease):
        #decreases the speed
        
        #if speed is greater than min speed decrease speed but do not decrease below min speed
        if self.__speed > self.__minimum_speed:
            self.__speed = self.__speed - speed_decrease
            if self.__speed < self.__minimum_speed:
                self.__speed = self.__minimum_speed
        else:
            print('Can not decrease speed below maximum reverse speed.')
    
    def current_state(self):
        #returns the current state of the vehicle
        
        return_string = "License plate number = " + str(self.__license_plate_number) + "\nColour = " + str(self.__colour) + "\nNumber of doors = " + str(self.__number_of_doors) + "\nSpeed = " + str(self.__speed) + "\nMaximum speed = " + str(self.__maximum_speed) + "\nMaximum speed in reverse = " + str(self.__minimum_speed) + "\nNumber of wheels = " + str(self.__number_of_wheels) + "\nNumber of tires = " + str(self.__number_of_tires) + "\n"
        
        return return_string
