from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width= 500,height= 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]


y_positions = [-160, -100, -40, 20, 80, 140]
all_turtles = []

# Create turtles dynamically
for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner! ")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()