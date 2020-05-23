from Bateria import Bateria
from Display import Display
from Operacoes import Operacoes
from TeclasCalculadora import TeclasCalculadora


class Calculadora():
    """Classe Calculadora
    """
    def __init__(self):
        self.bateria = Bateria()
        self.entrada = TeclasCalculadora()
        self.operacoes = Operacoes()
        self.display = Display()

    def novaOperacao(self, valor1, valor2):
        self.entrada.valorEntrada(valor1, valor2)
        self.bateria.uso()

    def soma(self):
        soma = self.operacoes.soma(self.entrada.getValor())
        self.display.mostraTexto(soma)
        self.bateria.uso()