def ComputeDiscount (Qty, Price, DiscountRt):
  ExtPrice = Qty * Price
  DiscountAmt = ExtPrice * DiscountRt
  DiscountPrice = ExtPrice - DiscountAmt
  return DiscountAmt,DiscountPrice
  
#input
Qty = float(input("Please enter quanity: "))
print("")
Price = float(input("Please enter price: "))
print("")
DiscountRt = float(input("Please enter discount amount: "))
print("")

DiscountAmt,DiscountPrice = ComputeDiscount(Qty, Price, DiscountRt)

#Output 
print("")
print("Quantity is: ",Qty)
print("")
print("Price is: ${:.2f}" .format (Price))
print("")
print("Discount Amount is: ${:.2f}" .format(DiscountAmt))
print("")
print("Discounted price is ${:.2f}" .format (DiscountPrice))