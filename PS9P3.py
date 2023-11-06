#counts
SumOfMSRP = 0
SumOfAllSalePrices = 0

#function
def CompOutTheDoorPrice (Make, Model, ElectricVehicleCode, MSRP):
  if ElectricVehicleCode == "y" or ElectricVehicleCode == "Y":
    PercentOffMSRP = .30
  elif Make == "Honda" and Model == "Accord":
    PercentOffMSRP = .10
  elif Make == "Toyota" and Model == "Rav4":
    PercentOffMSRP = .15
  else:
    PercentOffMSRP = .05
  OutTheDoorPrice = ((MSRP - (MSRP * PercentOffMSRP))+ (MSRP * .07))
  return OutTheDoorPrice

#enter loop?
Run = input("Do you want to run this process? (y/n): ")
print("")

#Loop
while Run == "y":
  Make = input("Please enter the Make of the car: ")
  Model = input("Please enter the Model of the car: ")
  ElectricVehicleCode = input("Please enter Electric Vehicle Code y/n: ")
  MSRP = float(input("Please enter the MSRP: "))
  print("")
  OutTheDoorPrice = CompOutTheDoorPrice (Make, Model, ElectricVehicleCode, MSRP)
  print ("Out the Door price is ${:.2f}" .format (OutTheDoorPrice))
  SumOfMSRP = SumOfMSRP + MSRP
  SumOfAllSalePrices = SumOfAllSalePrices + OutTheDoorPrice
  print("")
  Run = input("Do you want to run this process again? y/n: ")
  print("")
  
#out of the loop
print("Sum of all MSRPs is ${:.2f}" .format (SumOfMSRP))
print("Sum of all sale prices are ${:.2f}" .format (SumOfAllSalePrices))
  