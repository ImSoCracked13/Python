from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, max_speed=0, color='', model='', load_capability = 1):
        super().__init__(max_speed, color, model)
        self._load_capability = load_capability

    def fuel_effiency(self):
        return 100 / self._load_capability
    
    def __str__(self):
        return super().__str__() + f'load capability: {self._load_capability}'