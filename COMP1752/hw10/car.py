from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, max_speed=0, color='', model='', electric = bool, power = 1):
        super().__init__(max_speed, color, model)
        self._electric = electric
        self._power = power

    def fuel_effiency(self):
        if self._electric == True:
            return 100.0
        else:
            return 100 / self._power
        
    def __str__(self):
        return super().__str__() + f'fuel effiency: {self.fuel_effiency()}'