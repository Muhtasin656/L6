import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
no_size=6
side_length=70
angle=360/no_size
for i in range(no_size):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()