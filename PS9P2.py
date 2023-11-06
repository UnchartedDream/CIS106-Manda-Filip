def CompPaint (L,W,H):
  SqFt = ((2*L*W) + (2*W*H))
  GalPaint = (SqFt/50)
  return GalPaint

Rooms = 0
Paint4AllRms = 0

Run = input("Do you want to run this process? (y/n): ")
print("")

#Loop
while Run == "y":
  L = float(input("Please enter Length of walls: "))
  W = float(input("Please enter Width of walls: "))
  H = float(input("Please enter Height of walls: "))
  print ("")
  Rooms = Rooms+1
  GalPaint = CompPaint (L,W,H)
  Paint4AllRms = Paint4AllRms + GalPaint
  print("Gallons of paint needed for this room are: {:.1f}" .format (GalPaint))
  print("")
  Run = input("Do you want to run this process again? (y/n): ")
  print("")

#out of loop
print ("Number of rooms is: ", Rooms)
print("Gallons of paint needed to paint all rooms is: {:.1f}" .format (Paint4AllRms))