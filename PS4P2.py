#Input phase
qty = float(input("Please enter the quantity you wish to purchase "))
Item = str(input("Please enter A or B for the item you wish to purchase "))

#if statment phase
if Item == "A":
  UnitPrice = 10

else:
  UnitPrice = 20
#process phase
ExtendedPrice = float(qty * UnitPrice)

#Output phase
print(" ")
print("By purchasing", qty, "of", Item, "at the unit price of", UnitPrice)
print(" ")
print("Your extended price comes to", ExtendedPrice) 

  