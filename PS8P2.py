def CompBatAvg (NumOfHits, Bats):
  BatAvg = (NumOfHits / Bats)
  return BatAvg

PlayerCount = 0

Run = input("Do you want to compute Batting Average (y/n)?: ")

while Run == ("y"):
  print("")
  LastName = input("Please enter last name of player: ")
  print("")
  NumOfHits = float(input("Please enter number of hits: "))
  Bats = float(input("Please enter number of bats: "))
  BatAvg = CompBatAvg(NumOfHits,Bats)
  PlayerCount = PlayerCount + 1
  print (LastName,"has a batting average of ", BatAvg)
  print("")
  Run = input("Do you wish to comput another Batting Average? (y/n): ")

#out of loop
print("")
print("Number of players entered: ", PlayerCount)