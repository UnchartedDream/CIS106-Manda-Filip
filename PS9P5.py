#sums
SumOfMarket = 0
SumOfAssessed = 0

#Function
def CompAssessedValue (County, MarketValue):
  if County == "Cook":
    AssessedValuePercent = .90
  elif County == "DuPage":
    AssessedValuePercent = .80
  elif County == "McHenry":
    AssessedValuePercent = .75
  elif County == "Kane":
    AssessedValuePercent = .60
  else: 
    AssessedValuePercent = .70
  AssessedValue = (MarketValue * AssessedValuePercent)
  return AssessedValue

#Run?
Run = input("Do you want to run this program? (y/n): ")
print("")

#loop
while Run == "y" or Run == "Y":
  County = input("Please enter the county of the house: ")
  MarketValue = float(input("Please enter the Market Value of the house: "))
  print("")
  AssessedValue = CompAssessedValue (County, MarketValue)
  print ("Assessed Value is: ${:.2f}" .format (AssessedValue))
  SumOfMarket = SumOfMarket + MarketValue
  SumOfAssessed = SumOfAssessed + AssessedValue
  print("")
  Run = input("Would you like to run this program again? (y/n): ")
  print("")

#Out of loop
print("Sum of all Market vaules is: ${:.2f}" .format (SumOfMarket))
print("")
print("Sum of all Assessed Values is: ${:.2f}" .format (SumOfAssessed))