#Count/sums
TicketSum = 0

#Function
def CompTicPrice(Miles):
  if Miles >= 30:
    Price = 12
  elif Miles >= 20:
    Price = 10
  elif Miles >= 10:
    Price = 8
  else:
    Price = 5
  return Price 

#Ask
Run = input("Do you want to run this process? y/n?: ")
print("")

#loop
while Run == "y" or Run == "Y":
  LastName = input("Please enter your last name: ")
  Miles = float(input("Please enter the miles from downtown Chicago: "))
  Price = CompTicPrice(Miles)
  TicketSum = TicketSum + Price
  print("")
  print("Price of ticket is: ${:.0f}" .format(Price))
  print("")
  Run = input("Do you wish to run this process gain? y/n: ")
  print("")

print ("Sum of all ticket prices is: ${:.0f}" .format(TicketSum))
 