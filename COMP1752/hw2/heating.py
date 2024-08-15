class Heating:
    def init(self):
        self.name = "Heating"
        self.type = "Temperature"
        self.level = 1
        self.status = True
    # turn on
    def turn_on(self):
        self.status = True
        print("Heating is on")
    # turn off
    def turn_off(self):
        self.status = False
        print("Heating is off")
    # increase the temp
    def increase(self):
        self.status += 1
        print(f"Heating temperature has increased by {self.level}")
    # decrease the temp
    def decrease(self):
        self.status -= 1
        print(f"Heating temperature has decreased by {self.level}")