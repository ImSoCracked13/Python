class Car:
    def __init__(self):
        self.model = "Unknown"
        self.price = 00.00
        self.brand = "Unknown"
        self.speed = 0
    def show_info(self):
        print(self.model)
        print(self.price)
        print(self.brand)
        print(self.speed)


Lamborghini_Veneno = Car('Veneno', 3300000.00, 'Lamborghini', 355)
Devel_Sixteen = Car('Sixteen', 1700000.00, 'Devel', 550)
Ferrari__FXX_K = Car('FXX K', 4000000.00, 'Ferrari', 350)
Koenigsegg_Agera_RS = Car('Agera RS', 5000000.00, 'Koenigsegg', 400)


class ShowRoom:
    def __init__(self):
        self.cars = Car
        self.name = "Unknown"
        self.income = 0.0
    def show_car(self):
        status = True
        while True:
            print(self.cars)
            if len(self.cars) == 0:
                print("No cars in the showroom currently.")
                status = False
                break
    def add_car(self, c):
        self.cars.append()
        print("Car {c.name} has been added.")
    def ask_if(self, model):
        for c in model:
            if c.name not in self.name:
                print("Model {c.name} is not in the showroom. Sorry for the incovinience unexpectation")
                return
            elif c.name in self.name:
                print("Model {c.name} is in the showroom. Take a look at this good ride, good Sir/Ma'am")
                print("The price of this car is {c.price}.")
    def sell_car(self, model):
        self.model = []
        current_income = 0.0
        if model in self.cars:
            self.income =  current_income + self.cars[1] 
            print("The model has been sold, balance of the showroom has increased by {self.income}")


class ShowRoomProgram:
    def __init__(self):
        self.showroom = ShowRoom
    def print_menu():
        print("1. Show all cars.\
               2. Add new Car.\
               3. Sell a Car.\
               4. Show showroom income.")
    def get_option(self, c):
        option = 0
        cars = Car
        input(int('Please enter a number only included in the menu has shown.'))
        if option == 1:
            print(Car)
        elif option == 2:
            for c in cars:
                ShowRoom.add_car()
                print("Car {c.name} has been added")
            else:
                return
        elif option == 3:
            ShowRoom.sell_car()
            return
        elif option == 4:
            print("The current balance of the income for the showroom is {self.income}")
            return
    def do_task(option):
        ShowRoomProgram.get_option()



