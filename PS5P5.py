#input
LastName = input("Please enter last name: ")
Salary = float(input("Please enter salary: "))
JobLvl = float(input("Please enter job Level: "))

#if defining 
if JobLvl >= 10:
  BonusRate = .25
elif JobLvl > 4:
  BonusRate = .20
else:
  BonusRate = .10

#Processing phase
Bonus = Salary * BonusRate

#Output Phase
print("")
print("Last name: ", LastName)
print("")
print("Bonus: ${:.2f}" .format(Bonus))