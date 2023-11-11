from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Algerian', 20, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.new_score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score :{self.new_score} ", align=ALIGNMENT, font=FONT)
        self.hideturtle()



