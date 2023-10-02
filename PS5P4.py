#input phase
NumOfTix = float(input("Please enter how many tickets you wish to purchase: "))

#if defining phase
if NumOfTix >= 25:
  PricePerTix = 50
elif NumOfTix > 9:
  PricePerTix = 60
elif NumOfTix > 5:
  PricePerTix = 70
else: 
  PricePerTix = 75
  
#Process Phase
TotalCost = NumOfTix * PricePerTix

#Output Phase
print("")
print("Number of tickets purchased: {:.0f}" .format(NumOfTix))
print("")
print("Price per ticket: ${:.2f}" .format (PricePerTix))
print("")
print("Total cost is: ${:.2f}" .format(TotalCost))