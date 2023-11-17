import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle colour will win the race?").lower()

colors = ["purple", "blue", "red", "yellow", "green"]
pos_2 = 100
color_index = 0
all_turtles = []

for turtle_index in range(0, 5):
    freya = t.Turtle(shape="turtle")
    freya.penup()
    freya.color(colors[color_index])
    freya.goto(x=-230, y=pos_2)
    pos_2 -= 50
    color_index += 1
    all_turtles.append(freya)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        speed = random.randint(0, 10)
        turtle.forward(speed)


screen.exitonclick()
