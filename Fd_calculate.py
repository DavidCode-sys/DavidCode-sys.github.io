import math
def air_density_at_temp(temp_celsius, altitude_m):
    #Standard air density at sea level (kg/m^3)
    density_sea_level = 1.225  
    #Approximate temperature decrease per 1000m altitude (°C/1000m (6.5°C))
    lapse_rate = 0.0065
    temperature_at_altitude = temp_celsius - (lapse_rate * altitude_m)
    #The **4.2561 comes from the gas law and pressure altitude relationship (5.2561 - 1 (to account for the temperature ratio) this also assumes a constant lapse rate)) Note: also an estimate
    density = density_sea_level * (temperature_at_altitude / temp_celsius) ** 4.2561
    return density

def calculate_drag_force(temp, altitude, mass, radius, initial_height, initial_velocity):
    #Acceleration due to gravity (m/s^2) [Down]
    g = 9.81  
    air_density = air_density_at_temp(temp, altitude)
    #Cross sectional area of the ball (m^2)
    area = math.pi * (radius ** 2)
    #Drag coefficient for a sphere (Approximate according to google)
    drag_coefficient = 0.34  
    velocity = initial_velocity
    height = initial_height
    #Time step for simulation (seconds)
    dt = 0.01  
    
    #Height cant be 0m
    while height > 0:
        #Gravitational force (N)
        Fg = mass * g  
        #Drag force (N)
        Fd = 0.5 * air_density * (velocity ** 2) * drag_coefficient * area  
        net_force = Fg - Fd
        acceleration = net_force / mass
        velocity += acceleration * dt
        height -= velocity * dt      
    final_drag_force = 0.5 * air_density * (velocity ** 2) * drag_coefficient * area
    return final_drag_force, velocity

#Parameters for my ball
temp_room = 13  #Temperature of my room (°C)
altitude = 90  #Altitude of Ajax above sea level (m)
mass_ball = 0.272155  #Mass of ball (kg)
radius_ball = 0.1016  #Radius of ball (m)
initial_height = 2  #Initial height (m)
initial_velocity = 0  #Initial velocity (m/s) (rest)

drag_force, final_velocity = calculate_drag_force(temp_room, altitude, mass_ball, radius_ball, initial_height, initial_velocity)
print(round(drag_force,5), "N")
print(round(final_velocity,5), "m/s")
