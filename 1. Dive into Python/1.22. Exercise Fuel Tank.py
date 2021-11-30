from math import *
fuel_tank = int(input()); fuel_consumption = int(input()); trip_length = int(input())
needed_fuel = (trip_length/100)*fuel_consumption
fueled_times = ceil(needed_fuel/fuel_tank)
fueled_times_except_initial = fueled_times-1
print(fueled_times_except_initial); print("%.2f" %(fueled_times*fuel_tank-needed_fuel))
