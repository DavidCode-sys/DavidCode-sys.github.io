import turtle
import math

#Set up the screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Uniform Circular Motion - Ping Pong Ball")
screen.tracer(0)

#Initial values from problem
MASS = 0.0027  #kg
RADIUS = 30  #cm
ANGULAR_VELOCITY = 5  #rad/s

#Convert radius to pixels (assuming 1 cm = 3 pixels)
RADIUS_PX = RADIUS * 3

#Create turtle
main_dot = turtle.Turtle()
main_dot.shape("circle")
main_dot.color("red")
main_dot.shapesize(0.5)
main_dot.penup()

x_proj = turtle.Turtle()
x_proj.shape("circle")
x_proj.color("blue")
x_proj.shapesize(0.3)
x_proj.penup()

#Info display
info_display = turtle.Turtle()
info_display.hideturtle()
info_display.penup()
info_display.goto(-380, 260)
info_display.color("black")

#Create a turtle for the string
string_turtle = turtle.Turtle()
string_turtle.hideturtle()
string_turtle.color("black")

#Create a turtle for the force arrow
force_arrow = turtle.Turtle()
force_arrow.hideturtle()
force_arrow.color("green")
force_arrow.pensize(2)

#Draw circular path
path = turtle.Turtle()
path.hideturtle()

def draw_arrow(t, length):
    t.forward(length)
    t.left(135)
    t.forward(10)
    t.backward(10)
    t.right(135)
    t.right(135)
    t.forward(10)
    t.backward(10)
    t.left(135)

def calculate_centripetal_force():
    
    return MASS * (ANGULAR_VELOCITY ** 2) * (RADIUS / 100) #Convert radius to meters 

time = 0

def animate():
    global time, RADIUS_PX
    x = RADIUS_PX * math.cos(ANGULAR_VELOCITY * time)
    y = RADIUS_PX * math.sin(ANGULAR_VELOCITY * time)
    
    main_dot.goto(x, y)
    x_proj.goto(x, 0)
    
    #Update string
    string_turtle.clear()
    string_turtle.penup()
    string_turtle.goto(0, 0)
    string_turtle.pendown()
    string_turtle.goto(x, y)
    
    #Draw force arrow
    force_arrow.clear()
    force_arrow.penup()
    force_arrow.goto(x, y)
    angle = math.atan2(-y, -x)
    force_arrow.setheading(math.degrees(angle))
    force_arrow.pendown()
    draw_arrow(force_arrow, 30)  #Fixed length for constant angular velocity
    
    #Calculate centripetal force
    centripetal_force = calculate_centripetal_force()
    #Update info display
    info_display.clear()
    info_display.write(f"Mass: {MASS} kg\n"
                       f"String Length (Radius): {RADIUS} cm\n"
                       f"Angular Velocity: {ANGULAR_VELOCITY} rad/s\n"
                       f"Centripetal Force: {centripetal_force:.4f} N",
                       font=("Arial", 12, "normal"))
    screen.update()
    time += 0.1
    screen.ontimer(animate, 50)

#Explanation text
explanation = turtle.Turtle()
explanation.hideturtle()
explanation.penup()
explanation.goto(0, -300)
explanation.write("The green arrow represents the centripetal force,\n"
                  "always directed towards the center of the circle.\n"
                  "v (linear) = rad/s * radius\n"
                  "Fc = m * ac  ---> Fc = m * (v²/r)\n"
                  "Press 'm' to change mass, 'r' for radius, 'v' for velocity",
                  align="center", font=("Arial", 12, "normal"))

#Calculator functions
def update_mass():
    global MASS
    new_mass = screen.textinput("Mass", f"Current mass: {MASS} kg. Enter new mass (kg)")
    if new_mass:
        try:
            MASS = float(new_mass)
        except ValueError:
            print("Invalid input for mass. Using previous value.")
    screen.listen()  #Keeps listening after the dialog closes

def update_radius():
    global RADIUS, RADIUS_PX
    new_radius = screen.textinput("Radius", f"Current radius: {RADIUS} cm. Enter new radius (cm)")
    if new_radius:
        try:
            RADIUS = float(new_radius)
            RADIUS_PX = RADIUS * 3
            redraw_path()
        except ValueError:
            print("Invalid input for radius. Using previous value.")
    screen.listen()  #Keeps listening after the dialog closes

def update_angular_velocity():
    global ANGULAR_VELOCITY
    new_velocity = screen.textinput("Angular Velocity", f"Current angular velocity: {ANGULAR_VELOCITY} rad/s. Enter new angular velocity (rad/s)")
    if new_velocity:
        try:
            ANGULAR_VELOCITY = float(new_velocity)
        except ValueError:
            print("Invalid input for angular velocity. Using previous value.")
    screen.listen()  #Keeps listening after the dialog closes

def redraw_path():
    path.clear()
    path.penup()
    path.goto(0, -RADIUS_PX)
    path.pendown()
    path.circle(RADIUS_PX)

#Set up event listeners
screen.onkeypress(update_mass, "m")
screen.onkeypress(update_radius, "r")
screen.onkeypress(update_angular_velocity, "v")

screen.listen()

#Draw initial circular path
redraw_path()

#Draw and label x-axis
path.penup()
path.goto(-200, 0)
path.pendown()
path.forward(400)
path.stamp()
path.write("X-axis", font=("Arial", 12, "normal"))

animate()
turtle.done()
