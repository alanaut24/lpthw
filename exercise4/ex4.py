#create variable cars and assign value 100
cars = 100
#create variable space_in_a_car and assign float of 4.0
space_in_a_car = 4.0
#create a variable drivers and assign value 30
drivers = 30
#create variable passengers and assign value 90
passengers = 90
#create variable cars_not_driven and assign value cars -  drivers
cars_not_driven = cars - drivers
#create variable cars_driven and assign value drivers
cars_driven = drivers
#create variable carpool_capacity and assign value  cars_driven * space_in_a_car
carpool_capacity =  cars_driven * space_in_a_car
#create variablee average_passengers_per_car and assign value passengers / cars_driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#study drills
