from tkinter import *

fruit_prices = {
    'Apple': 0.5,
    'Banana': 0.25,
    'Orange': 0.3,
    'Mango': 1.0,
    'Grapes': 0.4
}

def cb_fruits_selected(*args):
    selected_fruit = fruit_var.get()
    
    fruit_price = fruit_prices[selected_fruit]
    
    lbl_price.config(text=f"Price: ${fruit_price:.2f}")

def btn_calculate_clicked():
    selected_fruit = fruit_var.get()
    quantity = int(txt_quantity.get())

    total_cost = fruit_prices[selected_fruit] * quantity

    total_cost_label.config(text=f"Total cost: ${total_cost:.2f}")

window = Tk()
window.title("Fruit Ordering System")


fruit_label = Label(window, text="Select a fruit:")
fruit_label.grid(row=0, column=0, sticky=W)

fruit_var = StringVar(window)
fruit_var.set('Apple')  


cb_fruits = OptionMenu(window,                 
                            fruit_var,              
                            *fruit_prices.keys(),   
                            command=cb_fruits_selected)   
cb_fruits.grid(row=0, column=1, sticky=W)


lbl_price = Label(window, text="Price: $0.00")
lbl_price.grid(row=0, column=2, sticky=W)


lbl_quantity = Label(window, text="Enter quantity:")
lbl_quantity.grid(row=1, column=0, sticky=W)


txt_quantity = Entry(window)
txt_quantity.grid(row=1, column=1, sticky=W)

btn_calculate = Button(window, text="Calculate Total", command=btn_calculate_clicked)
btn_calculate.grid(row=1, column=2)

total_cost_label = Label(window, text="Total cost: $0.00")
total_cost_label.grid(row=2, column=0, columnspan=3)

window.mainloop()