from vehicle import Vehicle

class Motorbike(Vehicle):
    def __init__(self, max_speed=0, color='', model='', sport_bike = bool):
        super().__init__(max_speed, color, model)
        self._sport_bike = sport_bike

    def fuel_effiency(self):
        if self._sport_bike == True:
            return 90.0
        else:
            return 70.0
        
    def __str__(self):
        return super().__str__() + f'fuel effiency: {self.fuel_effiency()}'