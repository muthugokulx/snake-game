from turtle import Screen,Turtle

screen = Screen()

screen.title("Snake Game")
screen.setup(width = 600, height=600)
screen.bgcolor("black")


startingPostion = [(0,0),(-20,0),(-40,0)]


for position in startingPostion :
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

screen.exitonclick()

