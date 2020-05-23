class Bateria():
    def __init__(self):
        self.pcBateria = 100
        self.gasto = 0.9
    
    def uso(self):
        self.pcBateria = self.pcBateria * self.gasto
        self.getBateriaFraca()
    
    def getBateriaFraca(self):
        print(f'Tem {str(self.pcBateria)} % de bateria.')
        if (self.pcBateria < 55):
            print('Bateria fraca')
            return True
        else:
            return False