#inputphase
fixedcost = float(input("Please enter fixed costs "))
priceprunit = float(input("Please enter price per unit "))
costprunit = float(input("Please enter cost per unit "))

#process phase
breakeven = (fixedcost / (priceprunit - costprunit))

#output phase
print("Your break even point is", breakeven)