import turtle
import math

bob = turtle.Turtle()

def polygon(t, length, side):
    t = turtle.Turtle()
    for item in range(side):
        t.fd(length)
        t.lt(360.0 / side)

def circle(t,r):
    t = turtle.Turtle()
    area = 2 * math.pi * r
    n = int(area / 3) + 1
    length = area / n
    polygon(t, n, int(length))



print('Escolha uma das opções abaixo: ')
print('1 - Circulo.')
print('2 - Demais polígonos.')
opcao = str(input())

if opcao == '1':
   r = int(input('Digite o raio do círculo: '))
   circle(bob, r)
else:
   side = int(input('Digite o número de lados do poligono será desenhado: '))
   length = int(input('Digite o tamanho do lado do polígono: '))
   polygon(bob, length, side)





turtle.mainloop()