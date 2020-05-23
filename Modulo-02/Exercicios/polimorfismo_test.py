class FormaGeometrica():
   
    def calcArea(self):
        pass

class Retangulo(FormaGeometrica):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcArea(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcArea(self):
        return self.raio * self.raio * 3.14
    
class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcArea(self):
        return (self.base * self.altura) / 2



quadrado1 = Retangulo(2, 2)
retangulo1 = Retangulo(3, 6)
circulo1 = Circulo(5)
triangulo1 = Triangulo(2, 4)

formas_geometricas = [quadrado1, retangulo1, circulo1, triangulo1]

for forma in formas_geometricas:
    print(forma.calcArea())