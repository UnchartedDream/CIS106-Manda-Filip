#input phase
HowManyBooksToOrder = float(input("Please enter how many books you want to order: "))
CostPerBook = float(input("Please enter the price of the books: "))

#if/process phase
Total = (HowManyBooksToOrder * CostPerBook)

if Total > float(50):
  Shipping = float(0)
else:
  Shipping = float(25)

#output phase
print("With a total of", Total, "your additional shipping fee is ", Shipping)