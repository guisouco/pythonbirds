"""Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1) Atributo de dado velocidade
2) Método acelerar, que deverá incremetar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
1) Método girar_a_direita
2) Método girar_a_esquerda
"""

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade +=1

    def frear(self):
        if self.velocidade >1:
            self.velocidade -=2
        elif self.velocidade ==1:
            self.velocidade -=1

class Direcao:
    def __init__(self, valor='Norte'):
        self.valor = valor

    def metodo_girar_a_direita(self):
        if self.valor =='Norte':
            self.valor='Leste'
        elif self.valor == 'Leste':
            self.valor ='Sul'
        elif self.valor =='Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'

    def metodo_girar_a_esquerda(self):
        if self.valor =='Norte':
            self.valor='Oeste'
        elif self.valor == 'Oeste':
            self.valor ='Sul'
        elif self.valor =='Sul':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Norte'

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.metodo_girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.metodo_girar_a_esquerda()


if __name__ == '__main__':

 motor = Motor()
 print(motor.velocidade)
 motor.acelerar()
 print(motor.velocidade)
 motor.acelerar()
 print(motor.velocidade)
 motor.acelerar()
 print(motor.velocidade)
 motor.frear()
 print(motor.velocidade)
 motor.frear()
 print(motor.velocidade)
 direcao = Direcao()
 print(direcao.valor)
 direcao.metodo_girar_a_direita()
 print(direcao.valor)
 direcao.metodo_girar_a_direita()
 print(direcao.valor)
 direcao.metodo_girar_a_direita()
 print(direcao.valor)
 direcao.metodo_girar_a_direita()
 print(direcao.valor)
 direcao.metodo_girar_a_esquerda()
 print(direcao.valor)
 direcao.metodo_girar_a_esquerda()
 print(direcao.valor)
 direcao.metodo_girar_a_esquerda()
 print(direcao.valor)
 direcao.metodo_girar_a_esquerda()
 print(direcao.valor)
 carro = Carro(direcao, motor)
 print(carro.calcular_velocidade())
 carro.acelerar()
 print(carro.calcular_velocidade())
 carro.acelerar()
 print(carro.calcular_velocidade())
 carro.frear()
 print(carro.calcular_velocidade())
 print(carro.calcular_direcao())
 carro.girar_a_direita()
 print(carro.calcular_direcao())
 carro.girar_a_esquerda()
 print(carro.calcular_direcao())
 carro.girar_a_esquerda()
 print(carro.calcular_direcao())
