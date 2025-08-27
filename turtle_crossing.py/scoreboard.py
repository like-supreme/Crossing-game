from turtle import Turtle

FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200 , 260)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.color("Black")
        self.clear()
        self.write(f"Level: {self.level}" , align="center" , font= FONT)

    def increase_level(self):
        if self.level <= 5:
            self.level += 1
            self.update_scoreboard()

    def game_over(self):
        self.goto(0 , 0)
        self.color("Black")
        self.write("GAME OVER", align="center", font=FONT)



    
