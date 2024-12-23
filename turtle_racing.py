from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

def draw_finish():

    finish_line = Turtle()
    finish_line.penup()
    finish_line.setpos(230,-100)
    finish_line.setheading(90)
    finish_line.pendown()
    finish_line.forward(200)
    finish_line.write("FINISH LINE")
    finish_line.hideturtle()

def race(mr_turtle):
    mr_turtle.forward(random.randint(10,100))


position_x = -230
position_y = -100

screen = Screen()

screen.setup(width=600,height=400)

draw_finish()

for turtle_index in range(6):
    
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.setpos(position_x,position_y)
    position_y +=40 
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race: blue/gren/purple/red ")

if user_bet:
    race_on = True

while race_on:
    for i in range(6):
        race(all_turtles[i])
        if all_turtles[i].pos()[0] >= 230:
            winner = all_turtles[i].color()[0]
            print(f"The winner is {winner}")

            if user_bet.lower() == winner:
                print("You won!")
             
            else:
                print("You lose")
            
          
            race_on = False
            break

screen.exitonclick()
