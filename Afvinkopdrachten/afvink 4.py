item1 = int(input("prijs 1e item?"))
item2 = int(input("prijs 2e item?"))
item3 = int(input("prijs 3e item?"))
item4 = int(input("prijs 4e item?"))
item5 = int(input("prijs 5e item?"))
subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * 0.07
eind = subtotal + tax
print (subtotal)
print (tax)
print (eind)
