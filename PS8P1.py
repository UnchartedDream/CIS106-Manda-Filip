#functions
def CompExtPrice(qty, unitprice):
  extendedprice = qty*unitprice
  if extendedprice > 10_000.00:
    discountamount = extendedprice * .10
  else:
    discountamount = 0.0

  return extendedprice

totalextprice = 0.0
r = input("Do you want to compute extended price (y/n)?: ")

while r == "y":
  qty = float(input("Enter quantity: "))
  unitprice = float(input("Enter unit price: "))
  extendedprice = CompExtPrice(qty, unitprice)
  totalextprice = totalextprice + extendedprice
  print("Extended Price is ${:.2f}" .format(extendedprice))
  r = input("Do you wnat to compute extended price (y/n)?: ")

print("Total Extended price is ${:.2f}" .format(totalextprice))