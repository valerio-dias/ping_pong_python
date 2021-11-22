from turtle import Turtle, Screen
from raquete import Raquete
from bola import Bola
from placar import Placar
import time
import pygame

tela = Screen()
tela.setup(width=800, height=600)
tela.bgcolor('darkgreen')
tela.title('Ping Pong')
tela.tracer(0)

d_raquete = Raquete((350, 0), 'red')
e_raquete = Raquete((-350, 0), 'blue')
bola = Bola()
placar = Placar()
# pg = pygame.init()
pygame.mixer.init()
som_raquete = pygame.mixer.Sound('paddle_sound.wav')

tela.listen()
tela.onkeypress(d_raquete.pra_cima, 'Up')
tela.onkeypress(d_raquete.pra_baixo, 'Down')
tela.onkeypress(e_raquete.pra_cima, 'w')
tela.onkeypress(e_raquete.pra_baixo, 's')

jogo_on = True

while jogo_on:
    tela.update()
    time.sleep(bola.move_velocidade)
    bola.move()
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.quique_y()

    if bola.distance(d_raquete) < 50 and bola.xcor() > 320 or bola.distance(e_raquete) < 50 and bola.xcor() < -320:
        som_raquete.play()
        bola.quique_x()

    if bola.xcor() > 380:
        bola.retorna_posicao()
        placar.marca_ponto_e()

    if bola.xcor() < -380:
        bola.retorna_posicao()
        placar.marca_ponto_d()

tela.exitonclick()
     

