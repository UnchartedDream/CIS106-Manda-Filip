#input/define before loop
SumOfAllDiscounts = 0
RunProgram = str(input( "Do you wish to continue? Please enter Yes or No: "))

#Loop
while RunProgram == "Yes":
  print("")
  Price = float(input("Please enter price of item: "))
  print("")
  Qty = float(input("Please enter the quantity of the item you are purchasing: "))
  print("")
  ExtPrice = float(Qty * Price)
  #if
  if ExtPrice > float(10000):
    Discount = float(.25)
  else:
    Discount = float(.10)
   #end if/define more/Processing
  DiscountAmount = float(ExtPrice * Discount)
  SumOfAllDiscounts = float(SumOfAllDiscounts + DiscountAmount)
  Total = float(ExtPrice - DiscountAmount)
  print("Extended prices is: ${:.2f}" .format(ExtPrice))
  print("")
  print("Discount on this purchase is: ${:.2f}" .format(DiscountAmount))
  print("")
  print("Total cost for this order is: ${:.2f}" .format(Total)) 
  print("")
  RunProgram = str(input( "Do you wish to continue? Please enter Yes or No: "))

#out of loop
print("")
print("Total sum of discounts is : ${:.2f}" .format(SumOfAllDiscounts))