def CompScoreAvrg (S1, S2, S3):
  Sum = (S1 + S2 + S3)
  Avrg = (Sum / 3)
  return Sum, Avrg

#inputs
LastName = input("Please enter last name of student: ")
S1 = float(input(f"Please enter 1st score for {LastName}: "))
S2 = float(input(f"Please enter 2nd score for {LastName}: "))
S3 = float(input(f"Please enter 3rd score for {LastName}: "))

#call function
Sum, Avrg = CompScoreAvrg (S1, S2, S3)

#outputs
print("")
print(f"Student {LastName}")
print("")
print("Total of all test scores is: ", Sum)
print("")
print("Averge of test scores is {:.2f}" .format (Avrg))

