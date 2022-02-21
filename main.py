from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time


# Window
screen = Screen()
screen.bgcolor("#000")
screen.setup(1000, 800)
screen.title("Breakout Game")
screen.tracer(0)
# Paddle
paddle = Paddle()
# Listen to the key
screen.listen()
# When left arrow key is pressed, run function left
screen.onkeypress(paddle.move_left, "Left")
# When left arrow key is pressed, run function left
screen.onkeypress(paddle.move_right, "Right")

# Ball
ball = Ball()

# A list of the colors that will be used to create the bricks
color_list = ["red", "orange", "yellow", "green", "blue"]

# Laying the bricks out with these initial coordinates
x_pos = -445
y_pos = 380

# Empty list that will keep track of how many bricks there are
all_bricks = []


# Lays out bricks horizontally
def bricks_placement(color, x, y):
    for j in range(9):
        block = Bricks()
        block.color(color)
        block.goto(x, y)
        # We increase X here to lay them out beside each other
        x += 110
        # Appending the bricks to the list
        all_bricks.append(block)


# Lays out bricks vertically
for i in color_list:
    bricks_placement(i, x_pos, y_pos)
    # Decrease Y to start another row
    y_pos -= 30


game = True
while game:
    # How fast the ball will move
    time.sleep(ball.ball_speed)
    screen.update()

    # Send ball towards paddle
    ball.start_game()

    # If the ball goes under the paddle
    if ball.ycor() < -400:
        game=False
        print("End Game")
        screen.bye()

    # Logic when ball touches paddle or top of border then bounce
    if ball.distance(paddle) < 80 and ball.ycor() < -345 or ball.ycor() > 380:
        ball.bounce_y()

    # Logic when ball touches side walls
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Logic when ball touches bricks
    for brick in all_bricks:
        if ball.distance(brick) < 50:
            ball.bounce_y()
            brick.hideturtle()
            all_bricks.remove(brick)

    # If all bricks are gone then user wins
    if len(all_bricks) == 0:
        game=False
        print("Victory!")
        screen.bye()


# Stop the window from closing
screen.exitonclick()
