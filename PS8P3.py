def CompMGP(MilesTravelled, Gal):
  MPG = MilesTravelled/Gal
  return MPG

NumTrips = 0

Run = input("Do you want to run this process? (y/n): ")
print("")

while Run == "y":
  DestCity = input("Please enter the destination City: ")
  MilesTravelled = float(input("Please enter the miles traveled for this trip: "))
  Gal = float(input("Please enter number of gallons of fuel used for this trip: "))
  MPG = CompMGP(MilesTravelled, Gal)
  NumTrips = NumTrips + 1 #count
  print("")
  print("Destiation\t\tMiles\t\tMPG")
  print(DestCity, "\t\t", MilesTravelled, "\t\t{:.2f}" .format(MPG)) 
  print("")
  Run = input("Do you want to run this process again? (y/n): ")
print("")
print("Number of entries")
print (NumTrips)