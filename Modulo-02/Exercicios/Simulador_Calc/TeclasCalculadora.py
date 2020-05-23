class TeclasCalculadora():
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
    
    def valorEntrada(self, v1, v2):
        self.valor1 = v1 
        self.valor2 = v2

    def getValor(self):
        return [self.valor1, self.valor2]
    