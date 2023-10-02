#input phase
PartNum = float(input("Please enter part number: "))
Qty = float(input("Please enter the quantity: "))

#if defining
if PartNum == 10 or PartNum ==  55:
  UnitCost = 1
elif PartNum == 99:
  UnitCost = 2
elif PartNum == 80 or PartNum ==  70:
  UnitCost = 3
else:
  UnitCost = 5
  
#processing phase
TotalCost = (Qty * UnitCost)

#Output phase
print("")
print("Part number: ", PartNum)
print("")
print("Unit cost is: ${:.2f}" .format(UnitCost))
print("")
print("Total cost is: ${:.2f}" .format(TotalCost))