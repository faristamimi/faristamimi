import turtle

import pixart


def test_turtle_move():
    pixart.turtle_move(50, 80)
    assert (turtle.xcor() == 50)
    assert (turtle.ycor() == 80)
