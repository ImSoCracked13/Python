import turtle as t

def polygon(n, side_length):
    turning_angle = 360 / n
    for i in range (1, n+1):
        t.forward(side_length)
        t.left(turning_angle)

def that_a_lot_of_polygons (n_poly, width, p_color, n, side_length):
    t.width(width)
    t.color(p_color)
    twisting_angle = 360 / n_poly
    for j in range (1, n_poly + 1):
        polygon(n, side_length)
        t.right(twisting_angle)
    t.exitonclick()

print("Hey! Welcome to yet another polygon-drawing program!")
print("Hope it does not suck.")
print("But I'm guaranteed it will be better than DOOM 2016 Polygon Gameplay :v")
print()

n = int(input("Type in the amount of sides of the polygon you want to draw: "))
print()
while n <= 2:
    print("Impossible Selection!")
    print()
    n = int(input("The amount of sides of the polygon you want to draw: "))
    print()

side_length = int(input("The length of the side of the polygon: "))
print()

while side_length <= 0:
    print("Impossible selection!")
    print()
    side_length = int(input("The length of the side of the polygon: "))
    print()

width = int(input("The width of the side of the polygon: "))
print()

while width <= 0:
    print("Impossible selection!")
    print()
    side_length = int(input("The width of the side of the polygon: "))
    print()

n_poly = int(input("The number of polygons: "))
print()

while n_poly <= 0:
    print("Impossible selection!")
    print()
    n_poly = int(input("The number of polygons: "))
    print()

p_color = input("The color of the sides of the polygons: ").lower()
that_a_lot_of_polygons(n_poly, width, p_color, n, side_length)
