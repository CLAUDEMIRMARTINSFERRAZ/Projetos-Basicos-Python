#Projeto 3 - Chutar um numero aleatorio.
#Objetivoi é cria um programa que gere um valor aleatorio e tentar descobri o numero correto.

import random

class ChuteONumero:
    def __init__ (self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 50
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print('Chute um valor mais baixo!')
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print('Chute um valor mais alto!')
                self.PedirValorAleatorio()
            if int(self.valor_do_chute) == self.valor_aleatorio:
                self.tentar_novamente =False
                print('PARABENS VOCÊ ACERTOU !!!')

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um numero:')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()