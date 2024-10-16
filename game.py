import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

#Main loop
if __name__ == "__main__":
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while True:

        # Update screen every "tick"
        screen.update()
        snake.move()
        time.sleep(0.1)

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # Detect collision with walls
        if snake.head.xcor() > 280 or snake.head.ycor() > 280 or\
            snake.head.ycor() < -280 or snake.head.xcor() < -280:
                # Game over
                scoreboard.game_over()
                break

        # Detect collition with self
        for segment in snake.body[1:]:
             if snake.head.distance(segment) < 10:
                  scoreboard.game_over()
                  break

    screen.exitonclick()