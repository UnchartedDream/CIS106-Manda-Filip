#input phase
purchaseprice = float( input("Please enter purchase price of stock "))
currentprice = float( input("Please enter the current price of stock "))
qty = float( input("Please enter the number of stocks purchased "))

#Process phase
value = ((currentprice - purchaseprice) * qty)

#output phase
print("Value of your stocks now is $", value)