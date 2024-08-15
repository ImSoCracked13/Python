

def list_pizza():
    pizza_types = ["Margherita", "Napoletana", "Marinara"]
    pizza_prices = [6.0, 7.0, 7.5]
    extra_types = ["Mushrooms", "Cheese", "Anchovies", "Sausage"]
    extra_prices = [0.5, 1.0, 1.5, 1.8]
    print(pizza_types, pizza_prices, extra_types, extra_prices)
    return pizza_types, pizza_prices, extra_types, extra_prices


def price_pizza_calculate(order):
    total_price = 0
    if(order == "Margherita"):
        total_price += 6.0
    elif(order == "Napoletana"):
        total_price += 7.0
    elif(order == "Marinara"):
        total_price += 7.5
    return total_price


def price_topping_calculate(order2):
    total_price = 0
    if(order2 == "Mushroom"):
        total_price += 0.5
    elif(order2 == "Cheese"):
        total_price += 1.0
    elif(order2 == "Anchovies"):
        total_price += 1.5
    elif(order2 == "Marinara"):
        total_price += 1.8
    return total_price


    
def take_order():
    total_price = 0
    order = input("What pizza you wanna redeem? ")
    order_line = price_pizza_calculate(order)
    order_amount = int(input("How many? "))
    total_price = order_line * order_amount
    
    order2 = input("Toppings? ")
    order2_line = price_topping_calculate(order2)
    total_price = total_price + order2_line

    print("Sir/Ma'am, here is yours serving price: ", total_price)

list_pizza()
take_order()













