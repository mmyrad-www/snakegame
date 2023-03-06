from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()


    def new_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.write("GAME OVER!", move=False, align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()
