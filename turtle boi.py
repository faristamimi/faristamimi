import turtle



def test_drive():
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.fillcolor()
    turtle.end_fill()

test_drive()
turtle.mainloop()