class Light:
    def init(self):
        self.name = "Light"
        self.type = "Brightness"
        self.level = 100
        self.status = True
    # turn on
    def turn_on(self):
        self.status = True
        print("Light is on")
    # turn off
    def turn_off(self):
        self.status = False
        print("Light is off")
    # increase the brightness
    def increase(self):
        self.status += 1
        print(f"Light brightness has increased by {self.level}")
    # decrease the brightness
    def decrease(self):
        self.status -= 1
        print(f"Light brightness has decreased by {self.level}")

