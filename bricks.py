from turtle import Turtle


# Creating one brick then will loop through them in main.py
class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
