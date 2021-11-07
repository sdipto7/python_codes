import turtle

bg = turtle.Screen()
bg.bgcolor('light green')
bg.title('My_turtle')

# square = turtle.Turtle()
# square.color('red')
# for i in range(4):
#     square.forward(50)
#     # my_turtle.backward(100)
#     square.right(90)
#     # print(square.position())
#     # print(square.heading())
    
# turtle.done()

# star = turtle.Turtle()
# star.color('blue')

# for i in range(5):
#     star.forward(50)
#     star.right(144)

# turtle.done()

hexagon = turtle.Turtle()
hexagon.color('brown')

side = 6
side_length = 70
angle = 360.00 / side

for i in range(side):
    hexagon.forward(side_length)
    hexagon.right(angle)

turtle.done()