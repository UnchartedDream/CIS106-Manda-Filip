def CompTuition(DistCode, CreditHrs):
  if DistCode == "I":
    CostPerCredit = 250
  elif DistCode == "O":
    CostPerCredit = 55
  else:
    CostPerCredit = 0
  Tuition = CostPerCredit * CreditHrs
  return Tuition

TotalTuition = 0

Run = input("Do you want to run this program? y/n?: ")
print("")

while Run == "y":
  LastName = input("Please enter last name of student: ")
  CreditHrs = float(input("Please enter number of credit hours taken: "))
  DistCode = input("Please enter District Code: ")
  Tuition = CompTuition(DistCode, CreditHrs)
  TotalTuition = Tuition + TotalTuition 
  print("")
  print(LastName)
  print("Tuition owed is: ${:.2f}" .format (Tuition))
  print("")
  Run = input("Do you want to run this program gain? y/n: ")
  print("")

print("Total tuition owed: ${:.2f}".format(TotalTuition))


