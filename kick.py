from math import *
density = 1.2 #kg/m**3
radius = 11 #cm
mass = 0.43 #kg
constant = 0.2
gravitational_acceleration = 9.81 #m/s**2
Area = pi*radius**2
Velocity_hard = 120 #km/hr
Velocity_soft = 10 #km/hr
gravitational_force = round(gravitational_acceleration * mass,1) #N
drag_force_soft = round(1/2*constant*density*Area*Velocity_soft**2,1) #N
drag_force_hard = round(1/2*constant*density*Area*Velocity_hard**2,1) #N
print(f'drag force hard: {drag_force_hard}N drag force soft:{drag_force_soft}N gravitational force:{gravitational_force} N')
ratio_hard = round(drag_force_hard/gravitational_force,1)
ratio_soft = round(drag_force_soft/gravitational_force,1)
print(f'ratio soft:{ratio_soft}, ratio hard: {ratio_hard}')


