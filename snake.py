from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.snake_body()

    def snake_body(self):
        x = 0
        for i in range(0, 3):
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(x, 0)
            x -= 20
            self.segments.append(new_square)

    def extend(self):
        add_square = Turtle("square")
        add_square.color("white")
        add_square.penup()
        add_square.goto(self.segments[len(self.segments)-1].pos())
        self.segments.append(add_square)

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_coordinate = self.segments[seg_num - 1].xcor()
            y_coordinate = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_coordinate, y_coordinate)
        self.segments[0].forward(20)

    def touching_body(self):
        for i in range(len(self.segments) - 1):
            if self.segments[0].xcor() == self.segments[i].xcor() and self.segments[0].ycor() == self.segments[i].ycor() :
                print("Game Over!")
                return True

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
