from menu import Menu
from car import Car
from motorbike import Motorbike
from truck import Truck


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