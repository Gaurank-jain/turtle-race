import turtle as t
import random


screen = t.Screen()
#screen.bgcolor("pink")
screen.setup(width=500, height=400)             # to set up the dimensions of the display or output window
race_is_on = False                              # this is to ensure that race doesn't start before user entering the input
color_list = ["violet", "blue", "green", "yellow", "orange", "red"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []                                # creating a list of all turtle


user_input=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color : ")
if user_input:
    race_is_on=True


for index in range(0,6):
    new_turtle = t.Turtle(shape ="turtle")
    new_turtle.color(color_list[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[index])
    all_turtles.append(new_turtle)


while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
