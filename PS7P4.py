#input-ish
f = open("PS7P4data.txt", "r")
sum_ext_price = float(0)
item = str(f.readline())
num_orders = 0

#start loop
while item != "":
  qty = float( f.readline())
  price = float( f.readline())
  print("Item is: ", item)
  print("Quantity of item is: {:.0f}" .format(qty))
  print("Price of item is ${:.2f}".format(price))
  ext_price = qty * price
  print("Extended price of ", item, " is ${:.2f}".format(ext_price))
  num_orders = num_orders +1
  sum_ext_price = ext_price + sum_ext_price
  print()
  item = str(f.readline())
f.close()

#Out of loop
print()
print("Number of orders: ", num_orders)
average_order = (sum_ext_price/num_orders)
print()
print("Sum of extended prices is: ${:.2f}".format(sum_ext_price))
print()
print("Averge cost of orders is: ${:.2f}".format(average_order))
