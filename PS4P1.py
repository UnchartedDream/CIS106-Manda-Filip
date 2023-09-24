#input phase
qty = float(input("Please enter the quantity you plan to purchase: "))

#if phase/input (things still need to be defince before they can be used)
if qty >= float(1000):
  UnitPrice = float(3)
if qty < float(1000):
  UnitPrice = float(5)

#Process phase
ExtendedPrice = (qty * UnitPrice)
Tax = (.07 * ExtendedPrice)
Total = (ExtendedPrice + Tax)


#Output
print("")
print("If you purchase", qty, "your unit price will be", UnitPrice)
print("")
print("This will make your Extended Price", ExtendedPrice, "with tax of", Tax, "being owed.")
print("")
print("This brings your Total to", Total)