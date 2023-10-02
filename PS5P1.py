#Input phase
Qty = float(input("Please enter the quantity of widgets: "))

#if phase to define
if Qty < 10000:
  Price = 10
  
elif Qty >= 50000:
  Price = 20
  
else:
  Price = 30

#other define/assign
ExtendedPrice = float(Qty * Price)
TaxAmount = (ExtendedPrice * .07)
Total = (ExtendedPrice + TaxAmount)

#Output phase
print("")
print("Your extended price is: ${:.2f}" .format (ExtendedPrice))
print("")
print("Your tax amount owed is: ${:.2f}".format(TaxAmount))
print("")
print("The total amount that you owe is: ${:.2f}".format(Total))