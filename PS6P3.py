#Input/define
LoopsRun = float(0)
RunProgram = str(input( "Do you wish to run this program? Please enter Yes or No: "))

#Loop
while RunProgram == "Yes":
  print("")
  LastName = str(input("Please enter the last name of the student: "))
  print("")
  Score1 = float(input("Please enter Exam score 1: "))
  print("")
  Score2 = float(input("Please enter Exam score 2: "))
  AverageScore = float((Score1 + Score2) / 2)
  print("")
  print("Last name of student is:", LastName)
  print("")
  print("Average score of exams is:", AverageScore)
  print("")
  LoopsRun = float(LoopsRun+1)
  print("Number of students who entered data:", LoopsRun)
  print("")
  RunProgram = str(input( "Do you wish to run this program again? Please enter Yes or No: "))
  