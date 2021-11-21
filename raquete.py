from turtle import Turtle

class Raquete(Turtle):
    def __init__(self, posicao, cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(cor)
        self.penup()
        self.goto(posicao)

    def pra_cima(self):
        novo_y = self.ycor() + 20
        self.goto(self.xcor(), novo_y)

    def pra_baixo(self):
        novo_y = self.ycor() - 20
        self.goto(self.xcor(), novo_y)