from turtle import Turtle, Screen,clear
import time
from snake import Snake
from food import Food
from scorecard import Scorecard,GameOver

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
score1= Scorecard()
game= GameOver

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_over= False
while not game_is_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food)<15:
        food.refresh()
        score1.new_score()
        snake.extend()
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280 :
        game_is_over=True
        clear()
        game()
    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments)<10:
            game_is_over=True
            game()











screen.exitonclick()