Total = 0
Tax = 0

def CompCosts(Qty, UnitPrice):
  global Total 
  Total = Qty * UnitPrice
  global Tax 
  Tax = .07 * Total
  return

#input
Qty = float(input("Please enter quantity: "))
UnitPrice = float(input("Please enter price of item(s): "))

#Call
CompCosts(Qty, UnitPrice)

#output
print("")
print("Total Cost is: ${:.2f}" .format(Total))
print("")
print("Tax is: ${:.2f}" .format (Tax))
