class Carro():
    def __init__(self):
        print("Criou um carro")
 
    def getMotor(self):
        print("tenho um motor a combustao")
 
class Taxi(Carro):
    def __init__(self):
        Carro.__init__(self)
        self.getMotor()
 
car = Taxi()