from math import *
mass = 67 #grms
density = 1.038 #grms/cm**3
specific_heat_capacity = 3.7 #J/grms*K
thermal_conductivity = 5.4*10**-3 #W/cm*K
Temp_boiling_water = 100 #C
Temp_original_egg = 4 #C
Room_temp = 20 #C
Temp_yoke = 70 #C
time_fridge_temp= ((mass**(2/3))*specific_heat_capacity*(density**(1/3)))/(thermal_conductivity*(pi**2)*((4*pi)/3)**(2/3)) \
                   *log(0.76*(Temp_original_egg-Temp_boiling_water)/(Temp_yoke-Temp_boiling_water))
time_room_temp= (mass**(2/3)*specific_heat_capacity*density**(1/3))/(thermal_conductivity*pi**2*((4*pi)/3)**(2/3))\
                *log(0.76*(Room_temp-Temp_boiling_water)/(Temp_yoke-Temp_boiling_water))

print(f'Room Temp egg:{time_room_temp}seconds Fridge Temp egg:{time_fridge_temp}seconds')
