from turtle import Turtle

class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.e_placar = 0
        self.d_placar = 0
        self.atualiza_placar()

    def atualiza_placar(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.e_placar}", align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.d_placar}", align="center", font=("Arial", 80, "normal"))

    def marca_ponto_e(self):
        self.e_placar += 1
        self.atualiza_placar()

    def marca_ponto_d(self):
        self.d_placar += 1
        self.atualiza_placar()