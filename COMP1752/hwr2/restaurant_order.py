from tkinter import *
from tkinter import messagebox as msb
from tkinter import ttk

class RestaurantOrder:
    def __init__(self):
        self.window = Tk()
        self.window.title("Restaurant Order")
        self.window.geometry("200x200")
        
        self.food_prices = {"Taco": 6.0, "Burger": 8.0, "Sandwich": 10.0, "Pizza": 12.0}
        
        self.lbl_main_dish =  Label(self.window, text="Main Dish:")
        self.lbl_main_dish.grid(row=0, column=0, sticky=E)
        
        self.main_dish_var = StringVar()
        self.cbb_main_dish = ttk.Combobox(self.window, width=5, values=list(self.food_prices.keys()), state='readonly', textvariable=self.main_dish_var)
        self.cbb_main_dish.grid(row=0, column=1)
        
        self.lbl_quantity = Label(self.window, text="Quantity:")
        self.lbl_quantity.grid(row=1, column=0, sticky=E)
        
        self.txt_quantity = Entry(self.window, width=3)
        self.txt_quantity.grid(row=1, column=1)
        
        self.fries_var = BooleanVar()
        self.cb_fries = Checkbutton(self.window, text="Fries($2)", variable=self.fries_var)
        self.cb_fries.grid(row=2, column=1)
        
        self.salad_var = BooleanVar()
        self.cb_salad = Checkbutton(self.window, text="Salad($3)", variable=self.salad_var)
        self.cb_salad.grid(row=3, column=1)
        
        self.soda_var = BooleanVar()
        self.cb_soda = Checkbutton(self.window, text="Soda($1)", variable=self.soda_var)
        self.cb_soda.grid(row=4, column=1)
        
        self.juice_var = BooleanVar()
        self.cb_juice = Checkbutton(self.window, text="Juice($1.5)", variable=self.juice_var)
        self.cb_juice.grid(row=5, column=1)
        
        self.btn_place_order = Button(self.window, text="Place Order", command=self.place_order)
        self.btn_place_order.grid(row=6, column=1)


    def place_order(self):
        try:
            main_dish = self.cbb_main_dish.get()
            quantity = int(self.txt_quantity.get())
            if quantity <= 0:
                msb.showerror("Error", "Enter a positive quantity!")
                return
            main_dish_price = self.food_prices.get(main_dish, 0.0) * quantity
            extras_price = 0 
            if self.fries_var == True:
                extras_price += 2.0
            if self.salad_var == True:
                extras_price += 3.0
            if self.soda_var == True:
                extras_price += 1.0
            if self.juice_var == True:
                extras_price += 1.5
            total_price = main_dish_price + extras_price
            msb.showinfo("Restaurant Order", f"You ordered {quantity} {main_dish}(s)\nTotal cost:${total_price}")
        except ValueError:
            msb.showerror("Error", "Invalid Information!")


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    program = RestaurantOrder()
    program.run()