class Display():
    def __init__(self):
        self.brilhoTela = 20
        self.textoTela = '0'

    def mostraTexto(self, textoTela):
        self.textoTela = textoTela
        print(self.textoTela)