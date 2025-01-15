import turtle
import math
#Calculator part for missing values
def calculate_snells_law(n1, n2, theta1, theta2):
    if n1 is None:
        return math.sin(math.radians(theta2)) * n2 / math.sin(math.radians(theta1))
    elif n2 is None:
        return math.sin(math.radians(theta1)) * n1 / math.sin(math.radians(theta2))
    elif theta1 is None:
        return math.degrees(math.asin(math.sin(math.radians(theta2)) * n2 / n1))
    elif theta2 is None:
        return math.degrees(math.asin(math.sin(math.radians(theta1)) * n1 / n2))

def draw_snells_law(n1, n2, theta1, theta2):
    screen.clear()
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.forward(400)
    t.penup()
    t.goto(0, -200)
    t.setheading(90)
    t.pendown()
    t.forward(400)
    t.color("red")
    t.penup()
    t.goto(0, 0)
    t.setheading(-theta1)
    t.pendown()
    t.forward(200)
    t.penup()
    t.goto(0, 0)
    t.color("blue")
    t.setheading(theta2)
    t.pendown()
    t.forward(200)
    
    t.penup()
    t.goto(-180, 150)
    t.write(f"n1 = {n1:.2f}", font=("Arial", 12, "normal"))
    t.goto(-180, 120)
    t.write(f"n2 = {n2:.2f}", font=("Arial", 12, "normal"))
    t.goto(-180, 90)
    t.write(f"θ1 = {theta1:.2f}°", font=("Arial", 12, "normal"))
    t.goto(-180, 60)
    t.write(f"θ2 = {theta2:.2f}°", font=("Arial", 12, "normal"))

def get_input(prompt):
    return turtle.textinput("Snell's Law Calculator", prompt)

def main():
    inputs = ["n1", "n2", "θ1 (degrees)", "θ2 (degrees)"]
    values = []
    for i, inp in enumerate(inputs):
        value = get_input(f"Enter {inp} (leave blank if unknown):")
        values.append(float(value) if value else None)
    n1, n2, theta1, theta2 = values
    
    if values.count(None) != 1:
        turtle.textinput("Error", "Please provide exactly three known values.")
        return
    #Set result as the result
    result = calculate_snells_law(n1, n2, theta1, theta2)
    if n1 is None:
        n1 = result
    elif n2 is None:
        n2 = result
    elif theta1 is None:
        theta1 = result
    elif theta2 is None:
        theta2 = result
    draw_snells_law(n1, n2, theta1, theta2)
    turtle.textinput("Result", f"Calculated Value: {result:.2f}")

screen = turtle.Screen()
screen.setup(500, 500)
screen.title("Snell's Law Calculator")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
main()
turtle.done()
