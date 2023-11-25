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
        file = open("data.txt")
        self.high_score = file.read()
        file.close()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score :{self.new_score}    High Score : {self.high_score} ", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def reset_score(self):
        if int(self.new_score) > int(self.high_score):
            self.high_score = str(self.new_score)
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.new_score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.new_score += 1
        self.update_score()

