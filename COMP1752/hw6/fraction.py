class Fraction:
    def __init__(self, n = 0, d = 0):
        self.numerator = n
        self.denominator = d
        while n != d:
            if n > d:
                n = n - d
            else:
                d = d - n
        return n
    def get_numerator(self):
        return self.numerator
    def get_denominmator(self):
        return self.denominator
    def set_numerator(self, n):
        self.__numerator = n
    def set_denominator(self, d):
        if d > 0:
            self.__denominator = d
        else:
            return
    def add(self, f):
        f = 0
        return self.__numerator * f.get_denominator() + self.__denominator * f.get.numerator(), self.__denominator * f.get_denominator()
    def sub(self, f):
        return self.__numerator * f.get_denominator() - self.__denominator * f.get.numerator(), self.__denominator * f.get_denominator()
    def mul(self, f):
        return self.__numerator * f.get_numerator(), self.denominator * f.get_denominator()
    def div(self, f):
        if f.get_numerator() == 0:
            return None
        return self.__numerator / f.get_denominator(), self.denominator * f.get_numerator()
    def show(self):
        print(self.__numerator, "/", self.__denominator, end="")


class DemoFraction:
    def __init__(self):
        self.f1 = 0
        self.f2 = 0
        self.f3 = 0
        self.f4 = 0
    def print_menu():
        print("Choose any number below to proceed the fraction calculation:\
                1. Addition.\
                2. Subtraction.\
                3. Multiplication.\
                4. Division.\
                5. End.")
        return
    def get_option():
        option = 0
        running = True
        while running:
            n1 = int(input("Enter first numerator: "))
            d1 = int(input("Enter first denominator: "))
            frac1 = Fraction(n1, d1)
            n2 = int(input("Enter second numerator: "))
            d2 = int(input("Enter second denominator: "))
            frac2 = Fraction(n2, d2)
            if option == 1:
                f1 = frac1.add(frac2)
                f1.show()
                print()
            elif option == 2:
                f2 = frac1.sub(frac2)
                f2.show()
                print()
            elif option == 3:
                f3 = frac1.mul(frac2)
                f3.show()
                print()
            elif option == 4:
                f4 = frac1.div(frac2)
                f4.show()
                print()
            elif option == 5:
                running = False
            else:
                return 
    def do_task():
        print(DemoFraction.print_menu())
        print(DemoFraction.get_option())
        return
