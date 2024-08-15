from tkinter import *

shipping_methods = {
    'Standard': 5.0,
    'Express': 10.0,
    'Priority': 15.0
}

def calculate_shipping():
    selected_method = var_shipping.get()
    weight = float(txt_weight.get())
    distance = float(txt_distance.get())
    
    if var_weight_unit.get() == 'Pounds':
        weight *= 0.45359237  
    
    if var_distance_unit.get() == 'Miles':
        distance *= 1.609344
    
    total_cost = (weight * 0.1) + (distance * 0.05) + shipping_methods[selected_method]
    
    lbl_total_cost.config(text=f"Total cost: ${total_cost:.2f}")

window = Tk()
window.title("Shipping Cost Calculator")

lbl_method = Label(window, text="Select a shipping method:")
lbl_method.grid(row=0, column=0, sticky=W)

var_shipping = StringVar(window)
var_shipping.set('Standard')  

cb_shipping = OptionMenu(window, var_shipping, *shipping_methods.keys(), \
                         command=calculate_shipping)
cb_shipping.grid(row=0, column=1, sticky=W)

lbl_weight = Label(window, text="Enter weight:")
lbl_weight.grid(row=1, column=0, sticky=W)

txt_weight = Entry(window)
txt_weight.grid(row=1, column=1, sticky=W)

var_weight_unit = StringVar(window)
var_weight_unit.set('Kilograms')  

lbl_weight_unit = Label(window, text="Weight unit:")
lbl_weight_unit.grid(row=2, column=0, sticky=W)

rd_kilograms = Radiobutton(window, text="Kilograms", variable=var_weight_unit, value='Kilograms')
rd_kilograms.grid(row=2, column=1, sticky=W)

rd_pounds = Radiobutton(window, text="Pounds", variable=var_weight_unit, value='Pounds')
rd_pounds.grid(row=2, column=2, sticky=W)

lbl_distance = Label(window, text="Enter distance:")
lbl_distance.grid(row=3, column=0, sticky=W)

txt_distance = Entry(window)
txt_distance.grid(row=3, column=1, sticky=W)

var_distance_unit = StringVar(window)
var_distance_unit.set('Kilometers')  

lbl_distance_unit = Label(window, text="Distance unit:")
lbl_distance_unit.grid(row=4, column=0, sticky=W)

rd_kilometers = Radiobutton(window, text="Kilometers", variable=var_distance_unit, \
                            value='Kilometers')
rd_kilometers.grid(row=4, column=1, sticky=W)

rd_miles = Radiobutton(window, text="Miles", variable=var_distance_unit, value='Miles')
rd_miles.grid(row=4, column=2, sticky=W)

btn_calculate = Button(window, text="Calculate", command=calculate_shipping)
btn_calculate.grid(row=5, column=1, sticky=W)

lbl_total_cost = Label(window, text="Total Shipping cost: $")
lbl_total_cost.grid(row=6, column=0, columnspan=3)

window.mainloop()