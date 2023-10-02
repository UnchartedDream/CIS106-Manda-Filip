#input phase
Principle = float(input("Please Enter Principle ammount: "))
YearsToMaturity = float(input("Please enter years to maturity: "))

#if defining phase
if Principle > 100000 and YearsToMaturity == 5:
  InterestRate = .06
elif Principle >= 50000 and YearsToMaturity == 10:
  InterestRate = .05
elif Principle >= 50000 and YearsToMaturity == 5:
  InterestRate = .04
else:
  InterestRate = .02

#process Phase
InterestFirstYear = Principle * InterestRate

#Output
print("")
print("Principle = ${:.2f}" .format(Principle))
print("")
print("Interest Rate = ${:.2f}" .format(InterestRate))
print("")
print("Interest earned in the first year = ${:.2f}" .format(InterestFirstYear))