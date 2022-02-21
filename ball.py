from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # Color of ball
        self.color("#fff")
        # Shape of ball
        self.shape("circle")
        # Penup so ball doesnt draw on canvas
        self.penup()
        # Creating a variable for the ball speed to later speed it up
        self.ball_speed = 0.1
        # Start the game with these coordinates
        self.x_move = 20
        self.y_move = 20

    # Ball will start moving towards the paddle
    def start_game(self):
        new_y = self.ycor() - self.y_move
        new_x = self.xcor() - self.x_move
        self.goto(new_x, new_y)

    # If ball touches paddle this function will be called
    def bounce_y(self):
        self.y_move *= -1
        # Ball speed gets faster
        # self.ball_speed *= 0.95

    # If ball touches x-axis this will be called
    def bounce_x(self):
        self.x_move *= -1
