from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        # Color of paddle
        self.color("#fff")
        # Shape of paddle
        self.shape("square")
        # Customize size and shape of paddle
        self.shapesize(stretch_wid=0.25, stretch_len=8)
        # Pen up so you don't draw when paddle moves
        self.penup()
        # Position of paddle
        self.goto(0, -370)

    # Move paddle right
    def move_right(self):
        self.forward(50)

    # Move paddle left
    def move_left(self):
        self.backward(50)
