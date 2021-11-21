from turtle import Turtle

class Bola(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_velocidade = 0.1

    def move(self):
        novo_x = self.xcor() + self.x_move
        novo_y = self.ycor() + self.y_move
        self.goto(novo_x, novo_y)

    def quique_y(self):
        self.y_move *= -1

    def quique_x(self):
        self.x_move *= -1
        self.move_velocidade *= 0.9

    def retorna_posicao(self):
        self.goto(0, 0)
        self.move_velocidade = 0.1
        self.quique_x()
        
  