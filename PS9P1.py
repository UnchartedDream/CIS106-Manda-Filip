Value = 0

def ForecastPercentCalc(Month):
  if Month == "Jan" or Month == "Feb" or Month == "Mar":
    ForecastPercent = .10
  elif Month == "Apr" or Month == "May" or Month == "Jun":
    ForecastPercent = .15
  elif Month == "July" or Month == "Aug" or Month == "Sep":
    ForecastPercent = .20
  elif Month == "Oct" or Month == "Nov" or Month == "Dec":
    ForecastPercent = .25
  else:
    ForecastPercent = 0
  return ForecastPercent

#Ask
Run = input("Do you want to run this program? y/n?: ")
print("")

#Loop
while Run == "y":
  LastName = input ("Please enter last name: ")
  Sales = float(input("Please enter sales amount: "))
  Month = input("Please enter the month: ")
  ForecastPercent = float(ForecastPercentCalc (Month))
  NextMonthSales = Sales * (1+ ForecastPercent) 
  print("")
  print("Next Month estimated sales are: ${:.2f}" .format (NextMonthSales))
  print("")
  print ("Forecast Percent is: ", ForecastPercent)
  Value = Value + NextMonthSales
  print("")
  Run = input("Do you want to run this program again? y/n?: ")
  print("")

#out of loop output
print("Value of all sales is: ${:.2f}" .format (Value))