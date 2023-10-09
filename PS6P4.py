#Define
RunProgram = str(input("Do you wish to run this program? Please enter Yes or No: "))
LoopRuns = float(0)

#Loop
while RunProgram == "Yes":
  print("")
  LastName = str(input("Please enter the last name of the employee: "))
  print("")
  HoursWorked = float(input("Please enter hours worked: "))
  print("")
  RateOfPay = float(input("Please enter rate of pay for employee: "))
  #loop-if
  if HoursWorked >40:
    OverTime = float((HoursWorked - 40) * (RateOfPay * .5))
  else:
    OverTime = 0
  GrossPay = float((RateOfPay * HoursWorked) + OverTime)
  print("")
  print("Last Name of employee:", LastName)
  print("")
  print("Gross pay for employee is:", GrossPay)
  print("")
  LoopRuns = float(LoopRuns + 1)
  print("Number of employees is:", LoopRuns)
  print("")
  RunProgram = str(input("Do you wish to run this program again? Please enter Yes or No: "))