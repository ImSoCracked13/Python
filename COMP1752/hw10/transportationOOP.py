from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, max_speed = 0, color = '', model = ''):
        self._max_speed = max_speed # km/h
        self._color = color
        self._model = model

    @property
    @abstractmethod
    def fuel_effiency(self):
        pass

    def __str__(self):
        return f'max speed: {self._max_speed} - color: {self._color} - model: {self._model}'


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


class Truck(Vehicle):
    def __init__(self, max_speed=0, color='', model='', load_capability = 1):
        super().__init__(max_speed, color, model)
        self._load_capability = load_capability

    def fuel_effiency(self):
        return 100 / self._load_capability
    
    def __str__(self):
        return super().__str__() + f'load capability: {self._load_capability}'
    

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


class Menu(ABC):
    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = self.get_option()
            self.do_task(choice)

            if choice == 0:
                running = False

    @abstractmethod
    def print_menu(self):
        pass

    def get_option(self):
        choice = int(input('Enter your choice: '))
        return choice
    
    @abstractmethod
    def do_task(self, choice):
        pass


class DemoTransport(Menu):
    def __init__(self):
        super().__init__()
        self.transport = []


    def print_menu(self):
        print("1. Add a car")
        print("2. Add an electric car")
        print("3. Add a truck")
        print("4. Add a motorbike")
        print("5. Display all vehicles")
        print("0. Quit")


    def add_car(self):
        a = int(input("Max speed: "))
        b = input("color: ")
        c = input("model: ")
        d = input('electric? :')
        e = int(input("power: "))
        if d == "Yes" or d == "yes":
            print("NO NO")
        else:
            new_car = Car(a, b, c, d, e)
            self.transport.append(new_car)


    def add_electric_car(self):
        a = int(input("Max speed: "))
        b = input("color: ")
        c = input("model: ")
        d = input('electric? :')
        e = int(input("power: "))
        if d == "No" or d == "No":
            print("NO NO")
        else:
            new_car = Car(a, b, c, d, e)
            self.transport.append(new_car)


    def add_truck(self):
        a = int(input("Max speed: "))
        b = input("color: ")
        c = input("model: ")
        d = int(input("load capability: "))
        new_truck = Truck(a, b, c, d)
        self.transport.append(new_truck)


    def add_motorbike(self):
        a = int(input("Max speed: "))
        b = input("color: ")
        c = input("model: ")
        d = bool(input("sport bike: "))
        new_motorbike = Motorbike(a, b, c, d)
        self.transport.append(new_motorbike)

    def show_all(self):
        print(self.transport)


    def get_option(self):
        choice = int(input('Enter your choice: '))
        return choice
    
    def do_task(self, choice):
        if choice == 1:
            self.add_car()
        if choice == 2:
            self.add_electric_car()
        if choice == 3:
            self.add_truck()
        if choice == 4:
            self.add_motorbike()
        if choice == 5:
            self.show_all()

    def run(self):
        return super().run()



system = DemoTransport()
system.run()