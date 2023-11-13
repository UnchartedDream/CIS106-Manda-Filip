def ComAvrgScore(S1, S2, S3, Handycap):
  Total = (S1+S2+S3)
  Avrg = Total/3
  AvrgWithH = Avrg + Handycap
  return Total, Avrg, AvrgWithH

#inputs
LastName = input("Please enter last name: ")
S1 = float(input("Please enter first score: "))
S2 = float(input("Please enter second score: "))
S3 = float(input("Please enter third score: "))
Handycap = float(input("Please enter Handycap: "))
print("")

#call
Total, Avrg, AvrgWithH = ComAvrgScore(S1, S2, S3, Handycap)

#Output
print(LastName)
print("")
print("Average Score is: {:.2f}".format(Avrg))
print("")
print("Average Score with Handycap is: {:.2f}".format(AvrgWithH))